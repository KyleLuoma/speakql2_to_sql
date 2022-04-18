from inspect import stack
from ntpath import join

from app.src.speakql_speech_recognition.FragmentElement import FragmentElement

from .AsrErrorHandler import *
from .SpeakQlPredictorCaller import *
from ..speakql_translator.SpeakQlTree import *
from .SpeakqlKeywords import *
from ..db_util.db_analyzer import *
from pyphonetics import Metaphone
from .QuerySegment import *
from .SegmentFragment import *
import pandas as pd
import multiprocessing as mp
import time

#Class used to handle unbundled queries at the sub-query level using multi-processing
class AsrMultiProcessor:

    def __init__(self, column_names, table_names, distinct_values):
        self.column_names = column_names
        self.table_names = table_names
        self.distinct_values = distinct_values
        self.max_lookahead = 4

    def process_multi_queries(self, asr_queries):
        
        mp_pool = mp.Pool(mp.cpu_count())
        results = mp_pool.map(self.do_processing_tasks, [query for query in asr_queries])
        mp_pool.close()
        return " AND THEN ".join(results)


    #This is the function that is included in the multiprocessing pool, and should be used
    #to define the operations performed on each subquery.
    def do_processing_tasks(self, query):

        query = query.replace(",", " ,")
        query = query.replace(".", " . ")
        query = query.replace("(", " ( ")
        query = query.replace(")", " ) ")
        query = query.replace("\"", " \" ")
        query = query.replace("'", " ' ")
        result = self.scan_query_with_parser(query)

        return result


    #This is the naive approach, we can use it as a baseline for more optimal methods.
    #Also, maybe use it as a last resort fallback if other methods fail to extract
    #a valid speakql query.
    def scan_query_with_parser(self, query):

        keywords = SpeakQlKeywords()
        spc = SpeakQlPredictorCaller()

        #Identify SFW structure within query
        words = query.split()
        speakql_query = ""
        print(words)

        #Start the process by finding the starting keyword at the beginning of the asr text
        for i in range(4, 0, -1):
            if i < len(words):
                candidate_phrase = " ".join(words[0 : i])
                if candidate_phrase in keywords.get_start_kws():
                    speakql_query = speakql_query + candidate_phrase
                    words = words[i  : ]
                    break
                elif i == 0:
                    speakql_query = speakql_query + candidate_phrase

        #scan the rest of the query:
        timeout = 30
        
        while len(words) > 0 and timeout > 0:
            added_word = False
            start_time = time.perf_counter()
            next_keywords = spc.getNextWordsFromQuery(speakql_query)
            end_time = time.perf_counter()
            #print("Time to fetch next words for", speakql_query, "is", str(end_time - start_time))
            
            for literal_kw in keywords.get_literal_kws():
                if literal_kw in next_keywords:
                    next_word_can_be_literal = True
                    next_keywords = next_keywords + self.table_names.TABLE_NAME.str.upper().to_list()
                    next_keywords = next_keywords + self.column_names.COLUMN_NAME.str.upper().to_list()

            #Be greedy, look ahead and consider joined string for multi-word keywords  (i.e. what is the)
            for i in range(self.max_lookahead, 0, -1):
                if (i) <= len(words):
                    candidate = " ".join(words[ : i])
                    #print("'" + candidate + "'")
                    if candidate in next_keywords:
                        speakql_query = speakql_query + " " + candidate
                        words = words[i  : ]
                        added_word = True
                        break
                    elif candidate.replace(" ", "") in next_keywords:
                        speakql_query = speakql_query + " " + candidate.replace(" ", "")
                        words = words[i  : ]
                        added_word = True
                        break
            
            if not added_word:
                timeout = timeout - 1

        if timeout == 0:
            print("WARNING: Query scan timed out!")
            print("TIMED OUT QUERY:", speakql_query)

        #print (next_keywords)
        return speakql_query




    def scan_select_expression(self, select_exp):
        pass

    

    def scan_from_expression(self, table_exp):
        pass



    def scan_where_expression(self, where_exp):
        pass



# Class used to convert an asr string into a valid speakql query
# Will contain several different methods for performing processing actions
class AsrStringProcessor:

    def __init__(self, db_analyzer):
        self.db_analyzer = db_analyzer
        self.predictor = SpeakQlPredictorCaller()
        self.keywords = SpeakQlKeywords()
        self.metaphone = Metaphone()

        print("Number of processors: ", mp.cpu_count())

        self.exp_delims = ["THEN"]

        self.word_similarity_method = "phonetic_distance"
        self.phonetic_distance_threshold = 1



    # This is the process driver. We'll start by doing everything in this method 
    # and may want to refactor to break it up later.
    def process_asr_string(self, asr_string):

        # ---- LEVEL 1: Break into segments using expression delimiter and validate, handle errors ----

        # Delimiter keyword clarification. Here we're 'clarifying' keywords by scanning the query
        # and raising any delimiter (i.e. AND THEN) keywords to uppercase. At this point, we want
        # to avoid introducing new errors, so we keep the edit distance threshold at 0.
        asr_string = self._clarify_l1_keywords(asr_string, dist_threshold=0)

        # Generate segments based on delimiter. Assume keywords are correct. We'll handle
        # resulting errors after this.
        query_segment_strings = self._separate_unbundled_query(asr_string)
        
        query_segments = []
        for segment_string in query_segment_strings:
            segment = QuerySegment(segment_string)
            segment.summary()
            query_segments.append(segment)

        # Handle L1 errors using the AsrErrorHandler
        error_handler = AsrErrorHandler()

        # Group consecutive errors, add to list, and pass to error handler
        error_segment_list = self._create_l1_error_segment_list(query_segments)
        error_handler.handle_l1_errors(error_segment_list, asr_string)


        # ---- LEVEL 2: Break into fragments using keywords and validate, handle errors ----
        for query_segment in query_segments:

            # L2 level keyword clarification. Again using 0 edit dist threshold to avoid introducing
            # new errors.
            query_segment.segment = self._clarify_l2_keywords(query_segment.segment, dist_threshold=0)

            # L2 level fragment generator
            fragment_list = self._separate_spj_parts(query_segment.segment)
            query_segment.append_fragments(fragment_list)
            for fragment in fragment_list:
                print(fragment.to_string())

            # Analyze fragments for error patterns:
            
            



        # ---- LEVEL 3: Break into elements using delimiters and validate, handle errors ----

            for query_segment in query_segments:
                for segment_fragment in query_segment.get_fragments():
                    # L3 keyword clarification. Using 0 edit dist threshold
                    fragment_string = self._clarify_l3_delimiters_in_fragment(segment_fragment.get_fragment_string(), ["AND", ","])

                    # Split into element strings TODO: Need to check fragment type and supply the appropriate delimiters
                    element_strings = self._separate_fragment_by_delimiters(fragment_string, ["AND", ","])
                    for element in element_strings:
                        print(element)
                        fragment_element = FragmentElement(element)
                        segment_fragment.append_element(fragment_element)


        segment_dicts = []
        for segment in query_segments:
            segment_dicts.append(segment.as_dict())

        # ---- RETURN: A dict with a list segments containing fragments and elements and unresolved errors ----
        return {
            "input_asr_string" : asr_string,
            "query_segments" : segment_dicts
        }

    
    # Receives a list of query segments, and groups the ones with errors into a list.
    # Returns a list of lists, where each list contains adjacent segments that have errors
    # If there is a segment without errors between to groups of error segments, that is 
    # what leads to creating a new segment list.
    def _create_l1_error_segment_list(self, query_segments):
        error_segment_list = []
        last_segment_had_error = False
        for segment in query_segments:
            if segment.has_errors() and not last_segment_had_error:
                error_segment_list.append([segment])
                last_segment_had_error = True
            elif segment.has_errors() and last_segment_had_error:
                error_segment_list[len(error_segment_list) - 1].append(segment)
                last_segment_had_error = True
            else:
                last_segment_had_error = False
        return error_segment_list



    #Calls ASR multi-process parallel processing method and the serial processing method
    # and prints a time comparison to the console.
    def parser_predictor_multi_vs_single_compare(self, asr_string):

        amp = AsrMultiProcessor(
            self.db_analyzer.get_column_names(),
            self.db_analyzer.get_table_names(),
            self.db_analyzer.get_distinct_values()
        )

        asr_string = asr_string.upper()
        
        start_time = time.perf_counter()
        asr_queries = self._separate_unbundled_query(asr_string)
        end_time = time.perf_counter()
        print("_separate_unbundled_query() time:", str(end_time - start_time), "seconds")

        start_time = time.perf_counter()
        results = amp.process_multi_queries(asr_queries)
        end_time = time.perf_counter()
        print("Process_multi_queries() time:", str(end_time - start_time), "seconds")
        print(results)

        start_time = time.perf_counter()
        print(amp.do_processing_tasks(asr_string))
        end_time = time.perf_counter()
        print("do_processing_tasks() (single processor) time:", str(end_time - start_time), "seconds")

        return results



    def _get_next_words(self, fragment):
        print(fragment)
        next_words = "hello" #self.predictor.getNextWordsFromQuery(fragment)
        return next_words



    #General method to compare word similarity. We can run experiments with different types of comparisons
    #using this method as the one location where we can make adjustments.
    def _check_word_similarity(self, word_one, word_two, phonetic_distance_threshold = 0):
        words_are_similar = False
        if self.word_similarity_method == "phonetic_distance":
            words_are_similar = self.metaphone.distance(
                self.metaphone.phonetics(word_one),
                self.metaphone.phonetics(word_two)
            ) <= phonetic_distance_threshold
        return words_are_similar
            


    #Pass in ASR transcript and make sure "and then" keywords are correct
    def _clarify_l1_keywords(self, asr_string, dist_threshold = 1):
        raw_string_words = asr_string.split(" ")
        string_words = []
        for word in raw_string_words:
            if len(word) > 0 and word != "\n":
                string_words.append(word)

        #use to keep track of candidate keywords in string_words
        keyword_candidates = []
        for i in range(0 , len(string_words)):
            keyword_candidates.append(False)


        #Find Levenstein distance between each keyword / keyword pair and l1 delims then or and then
        for keyword in self.keywords.get_exp_delim_kws():
            
            #Use to confirm that minimum required keywords to constitute a query exist in a fragment
            #before considering an L1 delim candidate (i.e. need a SELECT and FROM, or JOIN and WITH)
            select_kw = False
            from_kw = False
            join_kw = False
            with_kw = False
            select_modifiers = False

            fragment_is_query = (select_kw and from_kw) or (join_kw and with_kw) or select_modifiers
            
            num_keyword_in_phrase = len(keyword.split(" "))
            i = 0
            distance = dist_threshold + 1
            while (i + num_keyword_in_phrase) < len(string_words):
                asr_phrase = string_words[i]

                #Check if the asr_phrase word is a query keyword
                kw_type = self._get_kw_type(asr_phrase, dist_threshold=0)
                #print(asr_phrase, "is a", kw_type, "keyword." )
                if kw_type == "select":
                    select_kw = True
                elif kw_type == "from":
                    from_kw = True
                elif kw_type == "join":
                    join_kw = True
                elif kw_type == "with":
                    with_kw = True
                elif kw_type == "select_modifier":
                    select_modifiers = True

                words_are_similar = False

                fragment_is_query = (select_kw and from_kw) or (join_kw and with_kw) or select_modifiers

                if num_keyword_in_phrase > 1:
                    asr_phrase = asr_phrase + " " + string_words[i + 1]
                
                #Finding distance between phrase and keyword
                if len(asr_phrase) > 0:
                    words_are_similar = self._check_word_similarity(asr_phrase, keyword)  
                #If distance is below threshold, then we want to look ahead in the asr_string
                # to see if what follows is a starting keyword (or close to it).
                start_word_is_next = False
                if words_are_similar and (i + num_keyword_in_phrase + 1) < len(string_words):
                    for start_kw in self.keywords.get_start_kws():
                        if self._check_word_similarity(
                            string_words[i + num_keyword_in_phrase], 
                            start_kw.split(" ")[0],
                            dist_threshold
                            ):
                            start_word_is_next = True

                #First round of updates to keyword_candidates. We're not through though, we need to make
                #sure that between each keyword candidate there exists sufficient keywords to form a
                #sub query.
                if start_word_is_next and fragment_is_query:
                    word_num = 0
                    for word in asr_phrase.split(" "):
                        keyword_candidates[i + word_num] = True
                        string_words[i + word_num] = keyword.split()[word_num]
                        word_num = word_num + 1
                    fragment_is_query = False
                    select_kw = from_kw = join_kw = with_kw = select_modifiers = False
                i = i + 1
            #print(keyword_candidates)
            print("\n\n", "Output from L1 Clarification: \n"," ".join(string_words))
            return " ".join(string_words)



    #Scans a sub query for speakql keywords for level 2 structure determination. 
    #Simpler than the l1 process, so we should tighten up the dist_threshold to
    #avoid false positives.
    def _clarify_l2_keywords(self, asr_string, dist_threshold = 0):
        #Concatenate the lists of all keywords into one mega list:
        l2_keywords = (
            self.keywords.get_select_kws()
            + self.keywords.get_from_kws()
            + self.keywords.get_join_kws()
            + ["WHERE"] + ["ON"] + ["WITH"]
            + self.keywords.get_group_kws()
            + self.keywords.get_order_kws()
            + self.keywords.get_having_kws()
            + self.keywords.get_limit_kws()
        )
        string_words = asr_string.split()
        #Covering all different lengths of the keyword synonym phrases:

        for kw_len in range(5, 0, -1):
            
            #Iterating over all of the words in the sub query:
            for i in range(0, len(string_words) - (kw_len - 1)):
                fragment = " ".join(string_words[i : i + kw_len])
                #Iterate over all keywords in the mega list:
                for kw in l2_keywords:
                    #Compare the distance, and do replacement if below threshold
                    if (self.metaphone.distance(kw, fragment) <= dist_threshold 
                            and len(fragment) > 1
                            and fragment.upper() not in l2_keywords
                            and not fragment[0].isdigit()
                            ):
                        for j in range(i, i + len(kw.split(" "))):
                            if j < len(string_words):
                                string_words[j] = kw.split(" ")[j - i]
                    elif fragment.upper() in l2_keywords:
                        for j in range(i, i + len(fragment.split(" "))):
                            if j < len(string_words):
                                string_words[j] = fragment.split(" ")[j - i].upper()
        print("\n\n", "Output from L2 Clarification: \n"," ".join(string_words))
        return " ".join(string_words)



    # Identifies likely delimiters and replaces them with a valid delimiter keyword.
    # Generalized, so we need to pass in the appropriate delim_kws for the typ of
    # fragment that we are evaluating.
    def _clarify_l3_delimiters_in_fragment(self, asr_string, delim_kws, dist_threshold = 0):
        raw_string_words = asr_string.split(" ")
        string_words = []
        for word in raw_string_words:
            if len(word) > 0:
                string_words.append(word)
        ix = 0
        replaced = False
        for word in string_words:
            for delim_kw in delim_kws:
                if word.upper() not in delim_kws and self.metaphone.distance(word, delim_kw) <= dist_threshold:
                    string_words[ix] = delim_kw
                    break
                elif word.upper() in delim_kws:
                    string_words[ix] = word.upper()
                    break
            ix = ix + 1
        return " ".join(string_words)



    def _get_kw_type(self, keyword, dist_threshold = 0):
        keyword_type = "none" #options: "join", "with", "from", "select", "select_modifier"

        select_modifier_kws = (
                self.keywords.get_group_kws() 
                + self.keywords.get_limit_kws()
                + self.keywords.get_having_kws()
                + self.keywords.get_order_kws()
            )

        if len(keyword) > 0:
            for kw in self.keywords.get_from_kws():
                if self.metaphone.distance(kw.split(" ")[0], keyword) <= dist_threshold:
                    return "from"
            for kw in self.keywords.get_select_kws():
                if self.metaphone.distance(kw.split(" ")[0], keyword) <= dist_threshold:
                    return "select"
            for kw in self.keywords.get_join_kws():
                if self.metaphone.distance(kw.split(" ")[0], keyword) <= dist_threshold:
                    return "join"
            for kw in ["WITH"]:
                if self.metaphone.distance(kw.split(" ")[0], keyword) <= dist_threshold:
                    return "with"
            for kw in select_modifier_kws:
                if self.metaphone.distance(kw.split(" ")[0], keyword) <= dist_threshold:
                    return "select_modifier"
        return "none"

    

    #Perform L1 structure separation (do this after performing L1 clarification)
    def _separate_unbundled_query(self, asr_string):

        unbundled_queries = [asr_string]

        for keyword in self.keywords.get_exp_delim_kws():
            new_unbundled_queries = []
            for query in unbundled_queries:
                while keyword in query:
                    new_unbundled_queries.append(
                        query[ : query.find(keyword)].strip()
                    )
                    query = query[query.find(keyword) + len(keyword) : ]

                new_unbundled_queries.append(query.strip())

            unbundled_queries = new_unbundled_queries

        return unbundled_queries



    #Perform L2 structure separation (Do this after L1 and L2 clarification 
    # and L1 Structure Separation). Should not be used on queries with
    # subqueries. We need to pass a query through some sort of sub-query
    # masker before using this particular method.
    def _separate_spj_parts(self, unbundled_query):
        query_frag_list = []
        #Must be (has_select and hasfrom) or has_join_with to be a valid query fragment
        has_select = False
        has_from = False
        has_join_with = False

        string_words = unbundled_query.split(" ")
        ix = 0

        #Scan to find a select synonym and register the select expression in the dictionary
        select_fragment = self._find_query_fragments(
            unbundled_query = unbundled_query,  
            type_start_kw_list = self.keywords.get_select_kws(),
            max_kw_len = 3
        )
        select_fragment = self._clarify_l3_delimiters_in_fragment(
            select_fragment.strip(),
            ["AND", "COMMA"]
        )
        if len(select_fragment) > 0:
            has_select = True
            fragment = SegmentFragment("select", select_fragment)
            query_frag_list.append(fragment)

        #Scan to find a from synonym
        from_fragment = self._find_query_fragments(
            unbundled_query = unbundled_query,  
            type_start_kw_list = self.keywords.get_from_kws(),
            max_kw_len = 2
        )
        from_fragment = self._clarify_l3_delimiters_in_fragment(
            from_fragment.strip(),
            ["AND", "COMMA"]
        )
        if len(from_fragment) > 0:
            has_from = True
            fragment = SegmentFragment("from", from_fragment)
            query_frag_list.append(fragment)

        #Scan to find a single join_expression
        if(has_from and has_select):
            join_fragment = self._find_query_fragments(
                unbundled_query = unbundled_query,  
                type_start_kw_list = self.keywords.get_join_kws(),
                max_kw_len = 4
            )
            if len(join_fragment) > 0:
                fragment = SegmentFragment("join", join_fragment)
                query_frag_list.append(fragment)

        #Scan to find a group by expression
        group_by_fragment = self._find_query_fragments(
            unbundled_query = unbundled_query,
            type_start_kw_list = self.keywords.get_group_kws(),
            max_kw_len = 2
        )
        if len(group_by_fragment) > 0:
            fragment = SegmentFragment("group_by", group_by_fragment)
            query_frag_list.append(fragment)

        #Scan to find a having expression
        having_fragment = self._find_query_fragments(
            unbundled_query = unbundled_query,
            type_start_kw_list = self.keywords.get_having_kws(),
            max_kw_len = 1
        )
        if len(having_fragment) > 0:
            fragment = SegmentFragment("having", having_fragment)
            query_frag_list.append(fragment)

        #Scan to find an order by expression
        order_fragment = self._find_query_fragments(
            unbundled_query = unbundled_query,
            type_start_kw_list = self.keywords.get_order_kws(),
            max_kw_len = 2
        )
        if len(order_fragment) > 0:
            fragment = SegmentFragment("order_by", order_fragment)
            query_frag_list.append(fragment)

        #Scan to find a limit expression
        limit_fragment = self._find_query_fragments(
            unbundled_query = unbundled_query,
            type_start_kw_list = ["LIMIT"],
            max_kw_len = 1
        )
        if len(order_fragment) > 0:
            fragment = SegmentFragment("limit", limit_fragment)
            query_frag_list.append(fragment)

        #Scan to find a where synonym
        where_fragment = self._find_query_fragments(
            unbundled_query = unbundled_query,  
            type_start_kw_list = ["WHERE"],
            max_kw_len = 1
        )
        #Logical operators serve as our WHERE delimiter: AND XOR OR
        where_fragment = self._clarify_l3_delimiters_in_fragment(
            where_fragment.strip(),
            ["AND", "OR", "XOR"]
        )
        if len(where_fragment) > 0:
            fragment = SegmentFragment("where", where_fragment)
            query_frag_list.append(fragment)

        #If there is no valid SPJ query, then we need to find
        #a valid multi-join expression. At this point, we either have
        #a good multi-join query or we have an invalid query.
        has_with = "WITH" in unbundled_query
        has_join_kw = False
        for join_keyword in self.keywords.get_join_kws():
            if join_keyword in unbundled_query:
                has_join_kw = True
                break
        if has_join_kw and has_with and not(has_from or has_select):
            fragment = SegmentFragment("multi_join", unbundled_query)
            query_frag_list.append(fragment)

        #Now, if were get here and we still don't have a valid query, we 
        #need to return this in the dict as an "error" entry.
        if len(query_frag_list) == 0:
            fragment = SegmentFragment("error", unbundled_query)
            query_frag_list.append(fragment)
            

        return query_frag_list


    #This is for L3 separation, pass in the fragment and appropriate delimiters
    #and it will return a list. The first word of each list should be either
    #The beginning kw (SELECT, FROM, WHERE...) or the delimiter used in the query
    def _separate_fragment_by_delimiters(self, fragment, delim_kws):
        fragment = str(fragment.replace(",", " , "))
        # for kw in (self.keywords.get_start_kws() + ["WHERE"]):
        #     fragment = fragment.replace(kw, "")
        delimited_element_list = []
        current_fragment = ""
        ix = 0
        for word in fragment.split(" "):
            if word not in delim_kws and ix < len(fragment.split(" ")):
                current_fragment = current_fragment + " " + word
            if ix == len(fragment.split(" ")) - 1:
                delimited_element_list.append(current_fragment.strip())
            if word in delim_kws:
                delimited_element_list.append(current_fragment.strip())
                current_fragment = word
            
            ix = ix + 1
        return delimited_element_list

    

    # Find the beginning and end of a query fragment of a given type (i.e. select, 
    # from, where, join, multijoin). Return the fragment as a string. 
    # Returns string randing from fragment type start kw to any other start kw or the end of the query
    # (whichever appears first).
    def _find_query_fragments(self, unbundled_query, type_start_kw_list, max_kw_len = 3):

        string_words = unbundled_query.split(" ")
        ix = 0

        query_start = 0
        query_end = 0
        kw_in_query = ""
        has_fragment = False
        #Find the start index:
        for word in string_words:
            kw_phrase = ""
            for kw_len in range(max_kw_len, 0, -1):
                kw_phrase = " ".join(string_words[ix : ix + kw_len])
                if kw_phrase in type_start_kw_list:
                    has_fragment = True
                    query_start = ix
                    kw_in_query = kw_phrase
                    break
                kw_phrase = ""
            if has_fragment:
                break
            ix = ix + 1
        ix = 0
        #Find the end index:
        found_end = False
        if has_fragment:
            for word in string_words[query_start : ]:
                for start_kw in (self.keywords.get_start_kws() + ["WHERE"]):
                    if word == start_kw.split(" ")[0] and word not in kw_in_query.split(" "):
                        query_end = ix
                        found_end = True
                        break
                if found_end:
                    break
                ix = ix + 1
                #Check if we're at the end of the query:
                if ix == len(string_words[query_start : ]):
                    query_end = ix
            return " ".join(string_words[query_start : query_start + query_end])
        else:
            return ""



    # Simple find / replace using the symbols dict from SpeakqlKeywords
    # Use this in fragments that allow operations
    def replace_words_with_symbols(self, query):
        symbol_dict = self.keywords.get_symbols_dict()
        for text in self.keywords.get_symbol_text_list():
            if text in query:
                query = query.replace(text, symbol_dict[text])
        return query



    # Use the lexer to separate out all tokens and then join them back together
    # into a string. This helps us separate symbols from words, because ASR
    # tends to like to do things like add periods to the end of words and such.
    def get_tokenized_query_string_using_lexer(self, query):
        token_list = self.predictor.getLexerTokensFromQuery(query)
        return " ".join(token_list)

            

    




    
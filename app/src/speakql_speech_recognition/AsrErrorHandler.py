from pyphonetics import Metaphone

class AsrErrorHandler:

    def __init__(self):
        self.metaphone = Metaphone()

    # Search a string for word (or words) that sound like the keyword. return 
    # a list containing the replacement candidate and the keyword
    def find_word_sounds_like_keyword_in_string(self, asr_string, keyword, phonetic_distance_threshold = 1):
        num_kw_words = len(keyword.split(" "))
        asr_word_list = asr_string.split(" ")
        num_asr_words = len(asr_word_list)
        for i in range(0, num_asr_words - num_kw_words):
            asr_fragment = " ".join(asr_word_list[i : i + num_kw_words])
            words_are_similar = self.metaphone.distance(
                self.metaphone.phonetics(keyword),
                self.metaphone.phonetics(asr_fragment)
            ) <= phonetic_distance_threshold
            if words_are_similar:
                return [" ".join(asr_word_list[i : i + num_kw_words]), keyword]
        return ["",""]


    # Handle errors resulting from L1 separation and validation. 
    # errors: list of lists containing segments, i.e. [[segment, segment], [segment]]
    # asr_string: originating string containing unmodified text from ASR result
    def handle_l1_errors(self, errors, asr_string):
        
        # Analyze segments for error patterns:
        for error_group in errors:
            # Error pattern: partial (typically mis-interpreted keyword in segment)
            if len(error_group) == 1 and error_group[0].has_partial_error():
                print("ErrorHandler is handling a single partial error")
                segment = error_group[0]
                modified_segment_string = segment.get_segment_string()

                # Action 1: process segment to identify possible mis-interpreted keywords
                missing_keywords = segment.get_missing_keyword_list()
                replacement_candidates = []
                for keyword in missing_keywords:
                    replacement = self.find_word_sounds_like_keyword_in_string(segment.get_segment_string(), keyword)
                    if len(replacement[0]) > 0 and len(replacement[1]) > 0:
                        replacement_candidates.append(replacement)

                if len(replacement_candidates) == 1:
                    modified_segment_string = modified_segment_string.replace(
                        replacement_candidates[0][0], replacement_candidates[0][1]
                        )
                    print("Replaced", replacement_candidates[0][0], "with", replacement_candidates[0][1],
                          "in asr string", segment.get_segment_string(), "resulting in modified asr string", modified_segment_string
                    )

                # Action 2: if no valid query emerges from action 1, flag this segment for human clarification.


            # Error pattern: illegal keywords (typically missing or misinterpreted "and then" in segment)
            if len(error_group) == 1 and error_group[0].has_illegal_combination_error():
                print("ErrorHandler is handling an illegal keyword combination error")

            # Action 1: Check if there are enough keywords for two valid queries, if so, process 
            #           segment to identify possible "and then" delimiters
            #    approach a: look for "and then" phonemes (i.e. in then, and them, etc.)
            #    approach b: look for the natural junction between two valid segments 
            #                (a start keyword following a valid query)
            

            # Action 2: If two valid segments do not emerge from action 1, then consider false positive
            #           L2 keyword (i.e. IN instead of AND). 
            #    approach a: We need probabilistic replacement here. First, figure out which L2 keywords
            #                appear valid based on context, then predict the most likely alternate keyword
            #                for the apparently incorrectly interpreted keyword.


            
            # Error pattern: partial, illegal keywords (False positive "and then" in segment, 
            # spillover into next segment with false negative "and then")
            if len(error_group) == 2 and (
                error_group[0].has_partial_error() and error_group[1].has_illegal_combination_error()
            ):
                print("ErrorHandler is handling a partial + illegal keyword combination error")
            # Action 1: retrieve substring from ASR text that spans from beginning of partial to end 
            #           of illegal segment. Re-process this substring to separate into two valid queries.
            #    approach a: Ignore all "and then" keywords. Identify natural delimiting point. This would
            #                be following the presence of minimum required keywords and prior to a start
            #                keyword. Within this zone, search for "and then" candidates. If found, ignore
            #                all other "and then" keywords.


            # Error pattern: partial, partial (typically errant "and then" incorrectly separating a segment)
            if len(error_group) == 2 and (
                error_group[0].has_partial_error() and error_group[1].has_partial_error()
            ):
                print("ErrorHandler is handling a partial + partial error")
            # Action 1: Retrieve substring from ASR text that spans from beginning of first partial to end of
            #           the second partial. Ignore "and then" keyword candidates. Run validation on this string
            #           to see if it produces a valid L1 segment.

            # Action 2: If no valid l2 segment emerges, scan for L2 keyword candidates, experiment with replacements
            #           to see if we can produce a valid query segment.

            # Action 3: If no valid query is produced using L2 keyword replacement, then flag this segment for 
            #           human clarification.

            # Error pattern: illegal keywords, illegal_keywords 
            if len(error_group) == 2 and (
                error_group[0].has_illegal_combination_error() and error_group[1].has_illegal_combination_error()
            ):
                print("ErrorHandler is handling an illegal combination + illegal combination error")
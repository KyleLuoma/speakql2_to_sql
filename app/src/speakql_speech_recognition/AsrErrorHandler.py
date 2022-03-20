
class AsrErrorHandler:

    def __init__(self):
        pass


    # Handle errors resulting from L1 separation and validation. 
    # errors: list of lists containing segments, i.e. [[segment, segment], [segment]]
    # asr_string: originating string containing unmodified text from ASR result
    def handle_l1_errors(self, errors, asr_string):
        
        # Analyze segments for error patterns:
        for error_group in errors:
            # Error pattern: partial (typically mis-interpreted keyword in segment)
            if len(error_group) == 1 and error_group[0].has_partial_error():
                print("ErrorHandler is handling a single partial error")

            # Action 1: process segment to identify possible mis-interpreted keywords
            

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
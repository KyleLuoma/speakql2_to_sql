import subprocess
# import antlr4
# from antlr4.tree.Trees import Trees
from sys import platform
from os.path import exists

# from .antlr_builds.pySpeakQl.SpeakQlLexer import SpeakQlLexer
# from .antlr_builds.pySpeakQl.SpeakQlParser import SpeakQlParser
# from .antlr_builds.pySpeakQl.SpeakQlParserListener import SpeakQlParserListener
# from .antlr_builds.pySpeakQl.SpeakQlParserVisitor import SpeakQlParserVisitor



class SpeakQlParseCaller:

    def __init__(self, SpeakQlParseEngine):
        self.parse_engine = SpeakQlParseEngine

    def run_select_statement(self, query):
        return self.parse_engine.get_parse_tree("selectStatement", query)


class SpeakQlParseEngine:

    def __init__(self, build_name, simple_speakql = False):
        self.build_name = build_name
        self.simple_speakql = simple_speakql
        self.platform = platform

        self.parser_directory = ''

        if exists('./app/src/speakql_translator/parsecaller.config'):
            with open('./app/src/speakql_translator/parsecaller.config') as f:
                for line in f:
                    print(line)
                    if 'parser_directory' in line:
                        self.parser_directory = line.replace('parser_directory:', '').strip()


    def get_parse_tree(rule):
        tree = "()"
        return tree


class JavaSpeakQlParseEngine(SpeakQlParseEngine):

    def get_parse_tree(self, rule, query):
        if "linux" in self.platform and self.parser_directory == '':
            end_text = ["\\n\", stderr=b", "\\n', stderr=b"]
            working_directory = "/home/kyle/repos/speakql2_to_sql/app/bin/"
        elif self.parser_directory == '':
            end_text = ["\\r\\n"]
            working_directory = "c:/research_projects/speakql2_to_sql/app/bin/"
        else:
            end_text = ["\\n\", stderr=b", "\\n', stderr=b"]
            working_directory = self.parser_directory


        tree = subprocess.run(
            "java -jar speakql_predictor.jar -parse \"" + query.upper() +"\"", 
            capture_output=True,
            cwd=working_directory,
            shell=True
            )
        tree = str(tree)
        
        tree_start = tree.find("stdout=b") + len("stdout=b*")
        for text in end_text:
            possible_tree_end = tree.find(text)
            if possible_tree_end > 0:
                tree_end = possible_tree_end
        tree = tree[tree_start:tree_end]

        return tree

    def write_query_file(self, query, file_path):
        f = open(file_path, "w")
        f.write(query.upper())
        f.close()


# class PythonSpeakQlParseEngine(SpeakQlParseEngine):

#     def get_parse_tree(self, rule, query):
#         input_stream = antlr4.InputStream(query.upper())
#         lexer = SpeakQlLexer.SpeakQlLexer(input_stream)
#         token_stream = SpeakQlParser.CommonTokenStream(lexer)
#         parser = SpeakQlParser.SpeakQlParser(token_stream)
#         tree = parser.querySpecification()
#         tree_string = Trees.toStringTree(tree, None, parser)
#         return tree_string



    
import subprocess
import antlr4
from antlr4.tree.Trees import Trees
from sys import platform

from .antlr_builds.pySpeakQl.SpeakQlLexer import SpeakQlLexer
from .antlr_builds.pySpeakQl.SpeakQlParser import SpeakQlParser
from .antlr_builds.pySpeakQl.SpeakQlParserListener import SpeakQlParserListener
from .antlr_builds.pySpeakQl.SpeakQlParserVisitor import SpeakQlParserVisitor



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
        pass

    def get_parse_tree(rule):
        tree = "()"
        return tree


class JavaSpeakQlParseEngine(SpeakQlParseEngine):

    def get_parse_tree(self, rule, query):
        if "linux" in self.platform:
            print("LINUX") 
            end_text = "\\n', stderr=b"
            working_directory = "/home/kyle/repos/speakql2_to_sql/app/bin/"
        else:
            end_text = "\\r\\n"
            working_directory = "c:/research_projects/speakql2_to_sql/app/bin/"


        tree = subprocess.run(
            "java -jar speakql_predictor.jar -parse \"" + query.upper() +"\"", 
            capture_output=True,
            cwd="/home/kyle/repos/speakql2_to_sql/app/bin/",
            shell=True
            )
        tree = str(tree)
        tree_start = tree.find("stdout=b") + len("stdout=b*")
        tree_end = tree.find(end_text)
        tree = tree[tree_start:tree_end]
        return tree

    def write_query_file(self, query, file_path):
        f = open(file_path, "w")
        f.write(query.upper())
        f.close()


class PythonSpeakQlParseEngine(SpeakQlParseEngine):

    def get_parse_tree(self, rule, query):
        input_stream = antlr4.InputStream(query.upper())
        lexer = SpeakQlLexer.SpeakQlLexer(input_stream)
        token_stream = SpeakQlParser.CommonTokenStream(lexer)
        parser = SpeakQlParser.SpeakQlParser(token_stream)
        tree = parser.querySpecification()
        tree_string = Trees.toStringTree(tree, None, parser)
        return tree_string



    
import subprocess
import antlr4
from antlr4.tree.Trees import Trees

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
        pass

    def get_parse_tree(rule):
        tree = "()"
        return tree


class JavaSpeakQlParseEngine(SpeakQlParseEngine):

    def get_parse_tree(self, rule, query):
        query_path = "C:/research_projects/speakql2_to_sql/app/query.txt"
        self.write_query_file(query, query_path)
        simple = ""
        if self.simple_speakql: simple = "Simple" 
        tree = subprocess.run(
            "java org.antlr.v4.gui.TestRig " + simple + "SpeakQl " + rule + " -inputFile \"" + query_path + "\" -tree", 
            capture_output=True,
            cwd="c:/research_projects/speakql2_to_sql/app/src/speakql_translator/antlr_builds/" + self.build_name
            )
        tree = str(tree)
        tree_start = tree.find("stdout=b") + len("stdout=b*")
        tree_end = tree.find("\\r\\n")
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



    
import subprocess
import antlr4
import antlr_builds.pySpeakQl.SpeakQlLexer as SpeakQlLexer
import antlr_builds.pySpeakQl.SpeakQlParser as SpeakQlParser
import antlr_builds.pySpeakQl.SpeakQlParserListener as SpeakQlParserListener
import antlr_builds.pySpeakQl.SpeakQlParserVisitor as SpeakQlParserVisitor
from antlr4.tree.Trees import Trees


class SpeakQlParseCaller:

    def __init__(self, SpeakQlParseEngine):
        self.parse_engine = SpeakQlParseEngine

    def run_select_statement(self, query):
        return self.parse_engine.get_parse_tree("selectStatement", query)


class SpeakQlParseEngine:

    def __init__(self, build_name):
        self.build_name = build_name
        pass

    def get_parse_tree(rule):
        tree = "()"
        return tree


class JavaSpeakQlParseEngine(SpeakQlParseEngine):

    def get_parse_tree(self, rule, query):
        self.write_query_file(query)
        tree = subprocess.run(
            "java org.antlr.v4.gui.TestRig SpeakQl " + rule + " -inputFile \"../../query.txt\" -tree", 
            capture_output=True,
            cwd="c:/research_projects/speakql2_to_sql/antlr_builds/" + self.build_name
            )
        tree = str(tree)
        tree_start = tree.find("stdout=b") + len("stdout=b*")
        tree_end = tree.find("\\r\\n")
        tree = tree[tree_start:tree_end]

        return tree

    def write_query_file(self, query):
        f = open("query.txt", "w")
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



    
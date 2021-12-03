import antlr4
from antlr4.Recognizer import Recognizer
from antlr4.atn.ATN import ATN
from antlr4.tree.Trees import Trees
import antlr_builds.pySpeakQl.SpeakQlLexer as SpeakQlLexer
import antlr_builds.pySpeakQl.SpeakQlParser as SpeakQlParser
import antlr_builds.pySpeakQl.SpeakQlParserListener as SpeakQlParserListener
import antlr_builds.pySpeakQl.SpeakQlParserVisitor as SpeakQlParserVisitor
import speakql_to_sql

#query = "from (select a, b and c from table d) as source joined with table e show me source.a, sum(b) and avg(c) group by a"
query = "select a from update"

input_stream = antlr4.InputStream(query.upper())
lexer = SpeakQlLexer.SpeakQlLexer(input_stream)
token_stream = SpeakQlParser.CommonTokenStream(lexer)
parser = SpeakQlParser.SpeakQlParser(token_stream)

error_listener = SpeakQlParser.DiagnosticErrorListener()
parser.addErrorListener(error_listener)

tree = parser.querySpecification()
expected_tokens = antlr4.ATN.getExpectedTokens(parser.atn, stateNumber = 1, ctx = tree)
for token in expected_tokens:
    print(token)

print("Rule index:", tree.getRuleIndex())
print("Payload:", tree.getPayload())
print("RuleContext:", tree.getRuleContext())

tree_string = Trees.toStringTree(tree, None, parser)
print(speakql_to_sql.translate_speakql_to_sql(tree_string, verbose = False))




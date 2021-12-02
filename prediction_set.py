import antlr4
import antlr_builds.pySpeakQl.SpeakQlLexer as SpeakQlLexer
import antlr_builds.pySpeakQl.SpeakQlParser as SpeakQlParser
import antlr_builds.pySpeakQl.SpeakQlParserListener as SpeakQlParserListener
import antlr_builds.pySpeakQl.SpeakQlParserVisitor as SpeakQlParserVisitor

input_stream = antlr4.InputStream("FROM A SELECT B")
lexer = SpeakQlLexer.SpeakQlLexer(input_stream)
token_stream = SpeakQlParser.CommonTokenStream(lexer)
parser = SpeakQlParser.SpeakQlParser(token_stream)

error_listener = SpeakQlParser.DiagnosticErrorListener()
parser.addErrorListener(error_listener)

tree = parser.selectStatement()

antlr4.ATN.getExpectedTokens(stateNumber = -1, ctx = parser.querySpecification())


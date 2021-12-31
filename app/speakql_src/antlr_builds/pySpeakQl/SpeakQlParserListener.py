# Generated from SpeakQlParser.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SpeakQlParser import SpeakQlParser
else:
    from SpeakQlParser import SpeakQlParser

# This class defines a complete listener for a parse tree produced by SpeakQlParser.
class SpeakQlParserListener(ParseTreeListener):

    # Enter a parse tree produced by SpeakQlParser#root.
    def enterRoot(self, ctx:SpeakQlParser.RootContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#root.
    def exitRoot(self, ctx:SpeakQlParser.RootContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#sqlStatements.
    def enterSqlStatements(self, ctx:SpeakQlParser.SqlStatementsContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#sqlStatements.
    def exitSqlStatements(self, ctx:SpeakQlParser.SqlStatementsContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#sqlStatement.
    def enterSqlStatement(self, ctx:SpeakQlParser.SqlStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#sqlStatement.
    def exitSqlStatement(self, ctx:SpeakQlParser.SqlStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#emptyStatement.
    def enterEmptyStatement(self, ctx:SpeakQlParser.EmptyStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#emptyStatement.
    def exitEmptyStatement(self, ctx:SpeakQlParser.EmptyStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#ddlStatement.
    def enterDdlStatement(self, ctx:SpeakQlParser.DdlStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#ddlStatement.
    def exitDdlStatement(self, ctx:SpeakQlParser.DdlStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#dmlStatement.
    def enterDmlStatement(self, ctx:SpeakQlParser.DmlStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#dmlStatement.
    def exitDmlStatement(self, ctx:SpeakQlParser.DmlStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#transactionStatement.
    def enterTransactionStatement(self, ctx:SpeakQlParser.TransactionStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#transactionStatement.
    def exitTransactionStatement(self, ctx:SpeakQlParser.TransactionStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#replicationStatement.
    def enterReplicationStatement(self, ctx:SpeakQlParser.ReplicationStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#replicationStatement.
    def exitReplicationStatement(self, ctx:SpeakQlParser.ReplicationStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#preparedStatement.
    def enterPreparedStatement(self, ctx:SpeakQlParser.PreparedStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#preparedStatement.
    def exitPreparedStatement(self, ctx:SpeakQlParser.PreparedStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#compoundStatement.
    def enterCompoundStatement(self, ctx:SpeakQlParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#compoundStatement.
    def exitCompoundStatement(self, ctx:SpeakQlParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#administrationStatement.
    def enterAdministrationStatement(self, ctx:SpeakQlParser.AdministrationStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#administrationStatement.
    def exitAdministrationStatement(self, ctx:SpeakQlParser.AdministrationStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#utilityStatement.
    def enterUtilityStatement(self, ctx:SpeakQlParser.UtilityStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#utilityStatement.
    def exitUtilityStatement(self, ctx:SpeakQlParser.UtilityStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#createDatabase.
    def enterCreateDatabase(self, ctx:SpeakQlParser.CreateDatabaseContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#createDatabase.
    def exitCreateDatabase(self, ctx:SpeakQlParser.CreateDatabaseContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#createEvent.
    def enterCreateEvent(self, ctx:SpeakQlParser.CreateEventContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#createEvent.
    def exitCreateEvent(self, ctx:SpeakQlParser.CreateEventContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#createIndex.
    def enterCreateIndex(self, ctx:SpeakQlParser.CreateIndexContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#createIndex.
    def exitCreateIndex(self, ctx:SpeakQlParser.CreateIndexContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#createLogfileGroup.
    def enterCreateLogfileGroup(self, ctx:SpeakQlParser.CreateLogfileGroupContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#createLogfileGroup.
    def exitCreateLogfileGroup(self, ctx:SpeakQlParser.CreateLogfileGroupContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#createProcedure.
    def enterCreateProcedure(self, ctx:SpeakQlParser.CreateProcedureContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#createProcedure.
    def exitCreateProcedure(self, ctx:SpeakQlParser.CreateProcedureContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#createFunction.
    def enterCreateFunction(self, ctx:SpeakQlParser.CreateFunctionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#createFunction.
    def exitCreateFunction(self, ctx:SpeakQlParser.CreateFunctionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#createServer.
    def enterCreateServer(self, ctx:SpeakQlParser.CreateServerContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#createServer.
    def exitCreateServer(self, ctx:SpeakQlParser.CreateServerContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#copyCreateTable.
    def enterCopyCreateTable(self, ctx:SpeakQlParser.CopyCreateTableContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#copyCreateTable.
    def exitCopyCreateTable(self, ctx:SpeakQlParser.CopyCreateTableContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#queryCreateTable.
    def enterQueryCreateTable(self, ctx:SpeakQlParser.QueryCreateTableContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#queryCreateTable.
    def exitQueryCreateTable(self, ctx:SpeakQlParser.QueryCreateTableContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#columnCreateTable.
    def enterColumnCreateTable(self, ctx:SpeakQlParser.ColumnCreateTableContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#columnCreateTable.
    def exitColumnCreateTable(self, ctx:SpeakQlParser.ColumnCreateTableContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#createTablespaceInnodb.
    def enterCreateTablespaceInnodb(self, ctx:SpeakQlParser.CreateTablespaceInnodbContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#createTablespaceInnodb.
    def exitCreateTablespaceInnodb(self, ctx:SpeakQlParser.CreateTablespaceInnodbContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#createTablespaceNdb.
    def enterCreateTablespaceNdb(self, ctx:SpeakQlParser.CreateTablespaceNdbContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#createTablespaceNdb.
    def exitCreateTablespaceNdb(self, ctx:SpeakQlParser.CreateTablespaceNdbContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#createTrigger.
    def enterCreateTrigger(self, ctx:SpeakQlParser.CreateTriggerContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#createTrigger.
    def exitCreateTrigger(self, ctx:SpeakQlParser.CreateTriggerContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#createView.
    def enterCreateView(self, ctx:SpeakQlParser.CreateViewContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#createView.
    def exitCreateView(self, ctx:SpeakQlParser.CreateViewContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#createDatabaseOption.
    def enterCreateDatabaseOption(self, ctx:SpeakQlParser.CreateDatabaseOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#createDatabaseOption.
    def exitCreateDatabaseOption(self, ctx:SpeakQlParser.CreateDatabaseOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#ownerStatement.
    def enterOwnerStatement(self, ctx:SpeakQlParser.OwnerStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#ownerStatement.
    def exitOwnerStatement(self, ctx:SpeakQlParser.OwnerStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#preciseSchedule.
    def enterPreciseSchedule(self, ctx:SpeakQlParser.PreciseScheduleContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#preciseSchedule.
    def exitPreciseSchedule(self, ctx:SpeakQlParser.PreciseScheduleContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#intervalSchedule.
    def enterIntervalSchedule(self, ctx:SpeakQlParser.IntervalScheduleContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#intervalSchedule.
    def exitIntervalSchedule(self, ctx:SpeakQlParser.IntervalScheduleContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#timestampValue.
    def enterTimestampValue(self, ctx:SpeakQlParser.TimestampValueContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#timestampValue.
    def exitTimestampValue(self, ctx:SpeakQlParser.TimestampValueContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#intervalExpr.
    def enterIntervalExpr(self, ctx:SpeakQlParser.IntervalExprContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#intervalExpr.
    def exitIntervalExpr(self, ctx:SpeakQlParser.IntervalExprContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#intervalType.
    def enterIntervalType(self, ctx:SpeakQlParser.IntervalTypeContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#intervalType.
    def exitIntervalType(self, ctx:SpeakQlParser.IntervalTypeContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#enableType.
    def enterEnableType(self, ctx:SpeakQlParser.EnableTypeContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#enableType.
    def exitEnableType(self, ctx:SpeakQlParser.EnableTypeContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#indexType.
    def enterIndexType(self, ctx:SpeakQlParser.IndexTypeContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#indexType.
    def exitIndexType(self, ctx:SpeakQlParser.IndexTypeContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#indexOption.
    def enterIndexOption(self, ctx:SpeakQlParser.IndexOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#indexOption.
    def exitIndexOption(self, ctx:SpeakQlParser.IndexOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#procedureParameter.
    def enterProcedureParameter(self, ctx:SpeakQlParser.ProcedureParameterContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#procedureParameter.
    def exitProcedureParameter(self, ctx:SpeakQlParser.ProcedureParameterContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#functionParameter.
    def enterFunctionParameter(self, ctx:SpeakQlParser.FunctionParameterContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#functionParameter.
    def exitFunctionParameter(self, ctx:SpeakQlParser.FunctionParameterContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#routineComment.
    def enterRoutineComment(self, ctx:SpeakQlParser.RoutineCommentContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#routineComment.
    def exitRoutineComment(self, ctx:SpeakQlParser.RoutineCommentContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#routineLanguage.
    def enterRoutineLanguage(self, ctx:SpeakQlParser.RoutineLanguageContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#routineLanguage.
    def exitRoutineLanguage(self, ctx:SpeakQlParser.RoutineLanguageContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#routineBehavior.
    def enterRoutineBehavior(self, ctx:SpeakQlParser.RoutineBehaviorContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#routineBehavior.
    def exitRoutineBehavior(self, ctx:SpeakQlParser.RoutineBehaviorContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#routineData.
    def enterRoutineData(self, ctx:SpeakQlParser.RoutineDataContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#routineData.
    def exitRoutineData(self, ctx:SpeakQlParser.RoutineDataContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#routineSecurity.
    def enterRoutineSecurity(self, ctx:SpeakQlParser.RoutineSecurityContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#routineSecurity.
    def exitRoutineSecurity(self, ctx:SpeakQlParser.RoutineSecurityContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#serverOption.
    def enterServerOption(self, ctx:SpeakQlParser.ServerOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#serverOption.
    def exitServerOption(self, ctx:SpeakQlParser.ServerOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#createDefinitions.
    def enterCreateDefinitions(self, ctx:SpeakQlParser.CreateDefinitionsContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#createDefinitions.
    def exitCreateDefinitions(self, ctx:SpeakQlParser.CreateDefinitionsContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#columnDeclaration.
    def enterColumnDeclaration(self, ctx:SpeakQlParser.ColumnDeclarationContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#columnDeclaration.
    def exitColumnDeclaration(self, ctx:SpeakQlParser.ColumnDeclarationContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#constraintDeclaration.
    def enterConstraintDeclaration(self, ctx:SpeakQlParser.ConstraintDeclarationContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#constraintDeclaration.
    def exitConstraintDeclaration(self, ctx:SpeakQlParser.ConstraintDeclarationContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#indexDeclaration.
    def enterIndexDeclaration(self, ctx:SpeakQlParser.IndexDeclarationContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#indexDeclaration.
    def exitIndexDeclaration(self, ctx:SpeakQlParser.IndexDeclarationContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#columnDefinition.
    def enterColumnDefinition(self, ctx:SpeakQlParser.ColumnDefinitionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#columnDefinition.
    def exitColumnDefinition(self, ctx:SpeakQlParser.ColumnDefinitionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#nullColumnConstraint.
    def enterNullColumnConstraint(self, ctx:SpeakQlParser.NullColumnConstraintContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#nullColumnConstraint.
    def exitNullColumnConstraint(self, ctx:SpeakQlParser.NullColumnConstraintContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#defaultColumnConstraint.
    def enterDefaultColumnConstraint(self, ctx:SpeakQlParser.DefaultColumnConstraintContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#defaultColumnConstraint.
    def exitDefaultColumnConstraint(self, ctx:SpeakQlParser.DefaultColumnConstraintContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#visibilityColumnConstraint.
    def enterVisibilityColumnConstraint(self, ctx:SpeakQlParser.VisibilityColumnConstraintContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#visibilityColumnConstraint.
    def exitVisibilityColumnConstraint(self, ctx:SpeakQlParser.VisibilityColumnConstraintContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#autoIncrementColumnConstraint.
    def enterAutoIncrementColumnConstraint(self, ctx:SpeakQlParser.AutoIncrementColumnConstraintContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#autoIncrementColumnConstraint.
    def exitAutoIncrementColumnConstraint(self, ctx:SpeakQlParser.AutoIncrementColumnConstraintContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#primaryKeyColumnConstraint.
    def enterPrimaryKeyColumnConstraint(self, ctx:SpeakQlParser.PrimaryKeyColumnConstraintContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#primaryKeyColumnConstraint.
    def exitPrimaryKeyColumnConstraint(self, ctx:SpeakQlParser.PrimaryKeyColumnConstraintContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#uniqueKeyColumnConstraint.
    def enterUniqueKeyColumnConstraint(self, ctx:SpeakQlParser.UniqueKeyColumnConstraintContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#uniqueKeyColumnConstraint.
    def exitUniqueKeyColumnConstraint(self, ctx:SpeakQlParser.UniqueKeyColumnConstraintContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#commentColumnConstraint.
    def enterCommentColumnConstraint(self, ctx:SpeakQlParser.CommentColumnConstraintContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#commentColumnConstraint.
    def exitCommentColumnConstraint(self, ctx:SpeakQlParser.CommentColumnConstraintContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#formatColumnConstraint.
    def enterFormatColumnConstraint(self, ctx:SpeakQlParser.FormatColumnConstraintContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#formatColumnConstraint.
    def exitFormatColumnConstraint(self, ctx:SpeakQlParser.FormatColumnConstraintContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#storageColumnConstraint.
    def enterStorageColumnConstraint(self, ctx:SpeakQlParser.StorageColumnConstraintContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#storageColumnConstraint.
    def exitStorageColumnConstraint(self, ctx:SpeakQlParser.StorageColumnConstraintContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#referenceColumnConstraint.
    def enterReferenceColumnConstraint(self, ctx:SpeakQlParser.ReferenceColumnConstraintContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#referenceColumnConstraint.
    def exitReferenceColumnConstraint(self, ctx:SpeakQlParser.ReferenceColumnConstraintContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#collateColumnConstraint.
    def enterCollateColumnConstraint(self, ctx:SpeakQlParser.CollateColumnConstraintContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#collateColumnConstraint.
    def exitCollateColumnConstraint(self, ctx:SpeakQlParser.CollateColumnConstraintContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#generatedColumnConstraint.
    def enterGeneratedColumnConstraint(self, ctx:SpeakQlParser.GeneratedColumnConstraintContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#generatedColumnConstraint.
    def exitGeneratedColumnConstraint(self, ctx:SpeakQlParser.GeneratedColumnConstraintContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#serialDefaultColumnConstraint.
    def enterSerialDefaultColumnConstraint(self, ctx:SpeakQlParser.SerialDefaultColumnConstraintContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#serialDefaultColumnConstraint.
    def exitSerialDefaultColumnConstraint(self, ctx:SpeakQlParser.SerialDefaultColumnConstraintContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#checkColumnConstraint.
    def enterCheckColumnConstraint(self, ctx:SpeakQlParser.CheckColumnConstraintContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#checkColumnConstraint.
    def exitCheckColumnConstraint(self, ctx:SpeakQlParser.CheckColumnConstraintContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#primaryKeyTableConstraint.
    def enterPrimaryKeyTableConstraint(self, ctx:SpeakQlParser.PrimaryKeyTableConstraintContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#primaryKeyTableConstraint.
    def exitPrimaryKeyTableConstraint(self, ctx:SpeakQlParser.PrimaryKeyTableConstraintContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#uniqueKeyTableConstraint.
    def enterUniqueKeyTableConstraint(self, ctx:SpeakQlParser.UniqueKeyTableConstraintContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#uniqueKeyTableConstraint.
    def exitUniqueKeyTableConstraint(self, ctx:SpeakQlParser.UniqueKeyTableConstraintContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#foreignKeyTableConstraint.
    def enterForeignKeyTableConstraint(self, ctx:SpeakQlParser.ForeignKeyTableConstraintContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#foreignKeyTableConstraint.
    def exitForeignKeyTableConstraint(self, ctx:SpeakQlParser.ForeignKeyTableConstraintContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#checkTableConstraint.
    def enterCheckTableConstraint(self, ctx:SpeakQlParser.CheckTableConstraintContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#checkTableConstraint.
    def exitCheckTableConstraint(self, ctx:SpeakQlParser.CheckTableConstraintContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#referenceDefinition.
    def enterReferenceDefinition(self, ctx:SpeakQlParser.ReferenceDefinitionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#referenceDefinition.
    def exitReferenceDefinition(self, ctx:SpeakQlParser.ReferenceDefinitionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#referenceAction.
    def enterReferenceAction(self, ctx:SpeakQlParser.ReferenceActionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#referenceAction.
    def exitReferenceAction(self, ctx:SpeakQlParser.ReferenceActionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#referenceControlType.
    def enterReferenceControlType(self, ctx:SpeakQlParser.ReferenceControlTypeContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#referenceControlType.
    def exitReferenceControlType(self, ctx:SpeakQlParser.ReferenceControlTypeContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#simpleIndexDeclaration.
    def enterSimpleIndexDeclaration(self, ctx:SpeakQlParser.SimpleIndexDeclarationContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#simpleIndexDeclaration.
    def exitSimpleIndexDeclaration(self, ctx:SpeakQlParser.SimpleIndexDeclarationContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#specialIndexDeclaration.
    def enterSpecialIndexDeclaration(self, ctx:SpeakQlParser.SpecialIndexDeclarationContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#specialIndexDeclaration.
    def exitSpecialIndexDeclaration(self, ctx:SpeakQlParser.SpecialIndexDeclarationContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableOptionEngine.
    def enterTableOptionEngine(self, ctx:SpeakQlParser.TableOptionEngineContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableOptionEngine.
    def exitTableOptionEngine(self, ctx:SpeakQlParser.TableOptionEngineContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableOptionAutoIncrement.
    def enterTableOptionAutoIncrement(self, ctx:SpeakQlParser.TableOptionAutoIncrementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableOptionAutoIncrement.
    def exitTableOptionAutoIncrement(self, ctx:SpeakQlParser.TableOptionAutoIncrementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableOptionAverage.
    def enterTableOptionAverage(self, ctx:SpeakQlParser.TableOptionAverageContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableOptionAverage.
    def exitTableOptionAverage(self, ctx:SpeakQlParser.TableOptionAverageContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableOptionCharset.
    def enterTableOptionCharset(self, ctx:SpeakQlParser.TableOptionCharsetContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableOptionCharset.
    def exitTableOptionCharset(self, ctx:SpeakQlParser.TableOptionCharsetContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableOptionChecksum.
    def enterTableOptionChecksum(self, ctx:SpeakQlParser.TableOptionChecksumContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableOptionChecksum.
    def exitTableOptionChecksum(self, ctx:SpeakQlParser.TableOptionChecksumContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableOptionCollate.
    def enterTableOptionCollate(self, ctx:SpeakQlParser.TableOptionCollateContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableOptionCollate.
    def exitTableOptionCollate(self, ctx:SpeakQlParser.TableOptionCollateContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableOptionComment.
    def enterTableOptionComment(self, ctx:SpeakQlParser.TableOptionCommentContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableOptionComment.
    def exitTableOptionComment(self, ctx:SpeakQlParser.TableOptionCommentContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableOptionCompression.
    def enterTableOptionCompression(self, ctx:SpeakQlParser.TableOptionCompressionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableOptionCompression.
    def exitTableOptionCompression(self, ctx:SpeakQlParser.TableOptionCompressionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableOptionConnection.
    def enterTableOptionConnection(self, ctx:SpeakQlParser.TableOptionConnectionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableOptionConnection.
    def exitTableOptionConnection(self, ctx:SpeakQlParser.TableOptionConnectionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableOptionDataDirectory.
    def enterTableOptionDataDirectory(self, ctx:SpeakQlParser.TableOptionDataDirectoryContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableOptionDataDirectory.
    def exitTableOptionDataDirectory(self, ctx:SpeakQlParser.TableOptionDataDirectoryContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableOptionDelay.
    def enterTableOptionDelay(self, ctx:SpeakQlParser.TableOptionDelayContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableOptionDelay.
    def exitTableOptionDelay(self, ctx:SpeakQlParser.TableOptionDelayContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableOptionEncryption.
    def enterTableOptionEncryption(self, ctx:SpeakQlParser.TableOptionEncryptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableOptionEncryption.
    def exitTableOptionEncryption(self, ctx:SpeakQlParser.TableOptionEncryptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableOptionIndexDirectory.
    def enterTableOptionIndexDirectory(self, ctx:SpeakQlParser.TableOptionIndexDirectoryContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableOptionIndexDirectory.
    def exitTableOptionIndexDirectory(self, ctx:SpeakQlParser.TableOptionIndexDirectoryContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableOptionInsertMethod.
    def enterTableOptionInsertMethod(self, ctx:SpeakQlParser.TableOptionInsertMethodContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableOptionInsertMethod.
    def exitTableOptionInsertMethod(self, ctx:SpeakQlParser.TableOptionInsertMethodContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableOptionKeyBlockSize.
    def enterTableOptionKeyBlockSize(self, ctx:SpeakQlParser.TableOptionKeyBlockSizeContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableOptionKeyBlockSize.
    def exitTableOptionKeyBlockSize(self, ctx:SpeakQlParser.TableOptionKeyBlockSizeContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableOptionMaxRows.
    def enterTableOptionMaxRows(self, ctx:SpeakQlParser.TableOptionMaxRowsContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableOptionMaxRows.
    def exitTableOptionMaxRows(self, ctx:SpeakQlParser.TableOptionMaxRowsContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableOptionMinRows.
    def enterTableOptionMinRows(self, ctx:SpeakQlParser.TableOptionMinRowsContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableOptionMinRows.
    def exitTableOptionMinRows(self, ctx:SpeakQlParser.TableOptionMinRowsContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableOptionPackKeys.
    def enterTableOptionPackKeys(self, ctx:SpeakQlParser.TableOptionPackKeysContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableOptionPackKeys.
    def exitTableOptionPackKeys(self, ctx:SpeakQlParser.TableOptionPackKeysContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableOptionPassword.
    def enterTableOptionPassword(self, ctx:SpeakQlParser.TableOptionPasswordContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableOptionPassword.
    def exitTableOptionPassword(self, ctx:SpeakQlParser.TableOptionPasswordContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableOptionRowFormat.
    def enterTableOptionRowFormat(self, ctx:SpeakQlParser.TableOptionRowFormatContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableOptionRowFormat.
    def exitTableOptionRowFormat(self, ctx:SpeakQlParser.TableOptionRowFormatContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableOptionRecalculation.
    def enterTableOptionRecalculation(self, ctx:SpeakQlParser.TableOptionRecalculationContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableOptionRecalculation.
    def exitTableOptionRecalculation(self, ctx:SpeakQlParser.TableOptionRecalculationContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableOptionPersistent.
    def enterTableOptionPersistent(self, ctx:SpeakQlParser.TableOptionPersistentContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableOptionPersistent.
    def exitTableOptionPersistent(self, ctx:SpeakQlParser.TableOptionPersistentContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableOptionSamplePage.
    def enterTableOptionSamplePage(self, ctx:SpeakQlParser.TableOptionSamplePageContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableOptionSamplePage.
    def exitTableOptionSamplePage(self, ctx:SpeakQlParser.TableOptionSamplePageContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableOptionTablespace.
    def enterTableOptionTablespace(self, ctx:SpeakQlParser.TableOptionTablespaceContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableOptionTablespace.
    def exitTableOptionTablespace(self, ctx:SpeakQlParser.TableOptionTablespaceContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableOptionTableType.
    def enterTableOptionTableType(self, ctx:SpeakQlParser.TableOptionTableTypeContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableOptionTableType.
    def exitTableOptionTableType(self, ctx:SpeakQlParser.TableOptionTableTypeContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableOptionUnion.
    def enterTableOptionUnion(self, ctx:SpeakQlParser.TableOptionUnionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableOptionUnion.
    def exitTableOptionUnion(self, ctx:SpeakQlParser.TableOptionUnionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableType.
    def enterTableType(self, ctx:SpeakQlParser.TableTypeContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableType.
    def exitTableType(self, ctx:SpeakQlParser.TableTypeContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tablespaceStorage.
    def enterTablespaceStorage(self, ctx:SpeakQlParser.TablespaceStorageContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tablespaceStorage.
    def exitTablespaceStorage(self, ctx:SpeakQlParser.TablespaceStorageContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#partitionDefinitions.
    def enterPartitionDefinitions(self, ctx:SpeakQlParser.PartitionDefinitionsContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#partitionDefinitions.
    def exitPartitionDefinitions(self, ctx:SpeakQlParser.PartitionDefinitionsContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#partitionFunctionHash.
    def enterPartitionFunctionHash(self, ctx:SpeakQlParser.PartitionFunctionHashContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#partitionFunctionHash.
    def exitPartitionFunctionHash(self, ctx:SpeakQlParser.PartitionFunctionHashContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#partitionFunctionKey.
    def enterPartitionFunctionKey(self, ctx:SpeakQlParser.PartitionFunctionKeyContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#partitionFunctionKey.
    def exitPartitionFunctionKey(self, ctx:SpeakQlParser.PartitionFunctionKeyContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#partitionFunctionRange.
    def enterPartitionFunctionRange(self, ctx:SpeakQlParser.PartitionFunctionRangeContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#partitionFunctionRange.
    def exitPartitionFunctionRange(self, ctx:SpeakQlParser.PartitionFunctionRangeContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#partitionFunctionList.
    def enterPartitionFunctionList(self, ctx:SpeakQlParser.PartitionFunctionListContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#partitionFunctionList.
    def exitPartitionFunctionList(self, ctx:SpeakQlParser.PartitionFunctionListContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#subPartitionFunctionHash.
    def enterSubPartitionFunctionHash(self, ctx:SpeakQlParser.SubPartitionFunctionHashContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#subPartitionFunctionHash.
    def exitSubPartitionFunctionHash(self, ctx:SpeakQlParser.SubPartitionFunctionHashContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#subPartitionFunctionKey.
    def enterSubPartitionFunctionKey(self, ctx:SpeakQlParser.SubPartitionFunctionKeyContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#subPartitionFunctionKey.
    def exitSubPartitionFunctionKey(self, ctx:SpeakQlParser.SubPartitionFunctionKeyContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#partitionComparison.
    def enterPartitionComparison(self, ctx:SpeakQlParser.PartitionComparisonContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#partitionComparison.
    def exitPartitionComparison(self, ctx:SpeakQlParser.PartitionComparisonContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#partitionListAtom.
    def enterPartitionListAtom(self, ctx:SpeakQlParser.PartitionListAtomContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#partitionListAtom.
    def exitPartitionListAtom(self, ctx:SpeakQlParser.PartitionListAtomContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#partitionListVector.
    def enterPartitionListVector(self, ctx:SpeakQlParser.PartitionListVectorContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#partitionListVector.
    def exitPartitionListVector(self, ctx:SpeakQlParser.PartitionListVectorContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#partitionSimple.
    def enterPartitionSimple(self, ctx:SpeakQlParser.PartitionSimpleContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#partitionSimple.
    def exitPartitionSimple(self, ctx:SpeakQlParser.PartitionSimpleContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#partitionDefinerAtom.
    def enterPartitionDefinerAtom(self, ctx:SpeakQlParser.PartitionDefinerAtomContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#partitionDefinerAtom.
    def exitPartitionDefinerAtom(self, ctx:SpeakQlParser.PartitionDefinerAtomContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#partitionDefinerVector.
    def enterPartitionDefinerVector(self, ctx:SpeakQlParser.PartitionDefinerVectorContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#partitionDefinerVector.
    def exitPartitionDefinerVector(self, ctx:SpeakQlParser.PartitionDefinerVectorContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#subpartitionDefinition.
    def enterSubpartitionDefinition(self, ctx:SpeakQlParser.SubpartitionDefinitionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#subpartitionDefinition.
    def exitSubpartitionDefinition(self, ctx:SpeakQlParser.SubpartitionDefinitionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#partitionOptionEngine.
    def enterPartitionOptionEngine(self, ctx:SpeakQlParser.PartitionOptionEngineContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#partitionOptionEngine.
    def exitPartitionOptionEngine(self, ctx:SpeakQlParser.PartitionOptionEngineContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#partitionOptionComment.
    def enterPartitionOptionComment(self, ctx:SpeakQlParser.PartitionOptionCommentContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#partitionOptionComment.
    def exitPartitionOptionComment(self, ctx:SpeakQlParser.PartitionOptionCommentContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#partitionOptionDataDirectory.
    def enterPartitionOptionDataDirectory(self, ctx:SpeakQlParser.PartitionOptionDataDirectoryContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#partitionOptionDataDirectory.
    def exitPartitionOptionDataDirectory(self, ctx:SpeakQlParser.PartitionOptionDataDirectoryContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#partitionOptionIndexDirectory.
    def enterPartitionOptionIndexDirectory(self, ctx:SpeakQlParser.PartitionOptionIndexDirectoryContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#partitionOptionIndexDirectory.
    def exitPartitionOptionIndexDirectory(self, ctx:SpeakQlParser.PartitionOptionIndexDirectoryContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#partitionOptionMaxRows.
    def enterPartitionOptionMaxRows(self, ctx:SpeakQlParser.PartitionOptionMaxRowsContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#partitionOptionMaxRows.
    def exitPartitionOptionMaxRows(self, ctx:SpeakQlParser.PartitionOptionMaxRowsContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#partitionOptionMinRows.
    def enterPartitionOptionMinRows(self, ctx:SpeakQlParser.PartitionOptionMinRowsContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#partitionOptionMinRows.
    def exitPartitionOptionMinRows(self, ctx:SpeakQlParser.PartitionOptionMinRowsContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#partitionOptionTablespace.
    def enterPartitionOptionTablespace(self, ctx:SpeakQlParser.PartitionOptionTablespaceContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#partitionOptionTablespace.
    def exitPartitionOptionTablespace(self, ctx:SpeakQlParser.PartitionOptionTablespaceContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#partitionOptionNodeGroup.
    def enterPartitionOptionNodeGroup(self, ctx:SpeakQlParser.PartitionOptionNodeGroupContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#partitionOptionNodeGroup.
    def exitPartitionOptionNodeGroup(self, ctx:SpeakQlParser.PartitionOptionNodeGroupContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterSimpleDatabase.
    def enterAlterSimpleDatabase(self, ctx:SpeakQlParser.AlterSimpleDatabaseContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterSimpleDatabase.
    def exitAlterSimpleDatabase(self, ctx:SpeakQlParser.AlterSimpleDatabaseContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterUpgradeName.
    def enterAlterUpgradeName(self, ctx:SpeakQlParser.AlterUpgradeNameContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterUpgradeName.
    def exitAlterUpgradeName(self, ctx:SpeakQlParser.AlterUpgradeNameContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterEvent.
    def enterAlterEvent(self, ctx:SpeakQlParser.AlterEventContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterEvent.
    def exitAlterEvent(self, ctx:SpeakQlParser.AlterEventContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterFunction.
    def enterAlterFunction(self, ctx:SpeakQlParser.AlterFunctionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterFunction.
    def exitAlterFunction(self, ctx:SpeakQlParser.AlterFunctionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterInstance.
    def enterAlterInstance(self, ctx:SpeakQlParser.AlterInstanceContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterInstance.
    def exitAlterInstance(self, ctx:SpeakQlParser.AlterInstanceContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterLogfileGroup.
    def enterAlterLogfileGroup(self, ctx:SpeakQlParser.AlterLogfileGroupContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterLogfileGroup.
    def exitAlterLogfileGroup(self, ctx:SpeakQlParser.AlterLogfileGroupContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterProcedure.
    def enterAlterProcedure(self, ctx:SpeakQlParser.AlterProcedureContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterProcedure.
    def exitAlterProcedure(self, ctx:SpeakQlParser.AlterProcedureContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterServer.
    def enterAlterServer(self, ctx:SpeakQlParser.AlterServerContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterServer.
    def exitAlterServer(self, ctx:SpeakQlParser.AlterServerContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterTable.
    def enterAlterTable(self, ctx:SpeakQlParser.AlterTableContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterTable.
    def exitAlterTable(self, ctx:SpeakQlParser.AlterTableContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterTablespace.
    def enterAlterTablespace(self, ctx:SpeakQlParser.AlterTablespaceContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterTablespace.
    def exitAlterTablespace(self, ctx:SpeakQlParser.AlterTablespaceContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterView.
    def enterAlterView(self, ctx:SpeakQlParser.AlterViewContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterView.
    def exitAlterView(self, ctx:SpeakQlParser.AlterViewContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByTableOption.
    def enterAlterByTableOption(self, ctx:SpeakQlParser.AlterByTableOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByTableOption.
    def exitAlterByTableOption(self, ctx:SpeakQlParser.AlterByTableOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByAddColumn.
    def enterAlterByAddColumn(self, ctx:SpeakQlParser.AlterByAddColumnContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByAddColumn.
    def exitAlterByAddColumn(self, ctx:SpeakQlParser.AlterByAddColumnContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByAddColumns.
    def enterAlterByAddColumns(self, ctx:SpeakQlParser.AlterByAddColumnsContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByAddColumns.
    def exitAlterByAddColumns(self, ctx:SpeakQlParser.AlterByAddColumnsContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByAddIndex.
    def enterAlterByAddIndex(self, ctx:SpeakQlParser.AlterByAddIndexContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByAddIndex.
    def exitAlterByAddIndex(self, ctx:SpeakQlParser.AlterByAddIndexContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByAddPrimaryKey.
    def enterAlterByAddPrimaryKey(self, ctx:SpeakQlParser.AlterByAddPrimaryKeyContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByAddPrimaryKey.
    def exitAlterByAddPrimaryKey(self, ctx:SpeakQlParser.AlterByAddPrimaryKeyContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByAddUniqueKey.
    def enterAlterByAddUniqueKey(self, ctx:SpeakQlParser.AlterByAddUniqueKeyContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByAddUniqueKey.
    def exitAlterByAddUniqueKey(self, ctx:SpeakQlParser.AlterByAddUniqueKeyContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByAddSpecialIndex.
    def enterAlterByAddSpecialIndex(self, ctx:SpeakQlParser.AlterByAddSpecialIndexContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByAddSpecialIndex.
    def exitAlterByAddSpecialIndex(self, ctx:SpeakQlParser.AlterByAddSpecialIndexContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByAddForeignKey.
    def enterAlterByAddForeignKey(self, ctx:SpeakQlParser.AlterByAddForeignKeyContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByAddForeignKey.
    def exitAlterByAddForeignKey(self, ctx:SpeakQlParser.AlterByAddForeignKeyContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByAddCheckTableConstraint.
    def enterAlterByAddCheckTableConstraint(self, ctx:SpeakQlParser.AlterByAddCheckTableConstraintContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByAddCheckTableConstraint.
    def exitAlterByAddCheckTableConstraint(self, ctx:SpeakQlParser.AlterByAddCheckTableConstraintContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterBySetAlgorithm.
    def enterAlterBySetAlgorithm(self, ctx:SpeakQlParser.AlterBySetAlgorithmContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterBySetAlgorithm.
    def exitAlterBySetAlgorithm(self, ctx:SpeakQlParser.AlterBySetAlgorithmContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByChangeDefault.
    def enterAlterByChangeDefault(self, ctx:SpeakQlParser.AlterByChangeDefaultContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByChangeDefault.
    def exitAlterByChangeDefault(self, ctx:SpeakQlParser.AlterByChangeDefaultContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByChangeColumn.
    def enterAlterByChangeColumn(self, ctx:SpeakQlParser.AlterByChangeColumnContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByChangeColumn.
    def exitAlterByChangeColumn(self, ctx:SpeakQlParser.AlterByChangeColumnContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByRenameColumn.
    def enterAlterByRenameColumn(self, ctx:SpeakQlParser.AlterByRenameColumnContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByRenameColumn.
    def exitAlterByRenameColumn(self, ctx:SpeakQlParser.AlterByRenameColumnContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByLock.
    def enterAlterByLock(self, ctx:SpeakQlParser.AlterByLockContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByLock.
    def exitAlterByLock(self, ctx:SpeakQlParser.AlterByLockContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByModifyColumn.
    def enterAlterByModifyColumn(self, ctx:SpeakQlParser.AlterByModifyColumnContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByModifyColumn.
    def exitAlterByModifyColumn(self, ctx:SpeakQlParser.AlterByModifyColumnContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByDropColumn.
    def enterAlterByDropColumn(self, ctx:SpeakQlParser.AlterByDropColumnContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByDropColumn.
    def exitAlterByDropColumn(self, ctx:SpeakQlParser.AlterByDropColumnContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByDropConstraintCheck.
    def enterAlterByDropConstraintCheck(self, ctx:SpeakQlParser.AlterByDropConstraintCheckContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByDropConstraintCheck.
    def exitAlterByDropConstraintCheck(self, ctx:SpeakQlParser.AlterByDropConstraintCheckContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByDropPrimaryKey.
    def enterAlterByDropPrimaryKey(self, ctx:SpeakQlParser.AlterByDropPrimaryKeyContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByDropPrimaryKey.
    def exitAlterByDropPrimaryKey(self, ctx:SpeakQlParser.AlterByDropPrimaryKeyContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByRenameIndex.
    def enterAlterByRenameIndex(self, ctx:SpeakQlParser.AlterByRenameIndexContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByRenameIndex.
    def exitAlterByRenameIndex(self, ctx:SpeakQlParser.AlterByRenameIndexContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByAlterIndexVisibility.
    def enterAlterByAlterIndexVisibility(self, ctx:SpeakQlParser.AlterByAlterIndexVisibilityContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByAlterIndexVisibility.
    def exitAlterByAlterIndexVisibility(self, ctx:SpeakQlParser.AlterByAlterIndexVisibilityContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByDropIndex.
    def enterAlterByDropIndex(self, ctx:SpeakQlParser.AlterByDropIndexContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByDropIndex.
    def exitAlterByDropIndex(self, ctx:SpeakQlParser.AlterByDropIndexContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByDropForeignKey.
    def enterAlterByDropForeignKey(self, ctx:SpeakQlParser.AlterByDropForeignKeyContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByDropForeignKey.
    def exitAlterByDropForeignKey(self, ctx:SpeakQlParser.AlterByDropForeignKeyContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByDisableKeys.
    def enterAlterByDisableKeys(self, ctx:SpeakQlParser.AlterByDisableKeysContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByDisableKeys.
    def exitAlterByDisableKeys(self, ctx:SpeakQlParser.AlterByDisableKeysContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByEnableKeys.
    def enterAlterByEnableKeys(self, ctx:SpeakQlParser.AlterByEnableKeysContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByEnableKeys.
    def exitAlterByEnableKeys(self, ctx:SpeakQlParser.AlterByEnableKeysContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByRename.
    def enterAlterByRename(self, ctx:SpeakQlParser.AlterByRenameContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByRename.
    def exitAlterByRename(self, ctx:SpeakQlParser.AlterByRenameContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByOrder.
    def enterAlterByOrder(self, ctx:SpeakQlParser.AlterByOrderContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByOrder.
    def exitAlterByOrder(self, ctx:SpeakQlParser.AlterByOrderContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByConvertCharset.
    def enterAlterByConvertCharset(self, ctx:SpeakQlParser.AlterByConvertCharsetContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByConvertCharset.
    def exitAlterByConvertCharset(self, ctx:SpeakQlParser.AlterByConvertCharsetContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByDefaultCharset.
    def enterAlterByDefaultCharset(self, ctx:SpeakQlParser.AlterByDefaultCharsetContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByDefaultCharset.
    def exitAlterByDefaultCharset(self, ctx:SpeakQlParser.AlterByDefaultCharsetContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByDiscardTablespace.
    def enterAlterByDiscardTablespace(self, ctx:SpeakQlParser.AlterByDiscardTablespaceContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByDiscardTablespace.
    def exitAlterByDiscardTablespace(self, ctx:SpeakQlParser.AlterByDiscardTablespaceContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByImportTablespace.
    def enterAlterByImportTablespace(self, ctx:SpeakQlParser.AlterByImportTablespaceContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByImportTablespace.
    def exitAlterByImportTablespace(self, ctx:SpeakQlParser.AlterByImportTablespaceContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByForce.
    def enterAlterByForce(self, ctx:SpeakQlParser.AlterByForceContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByForce.
    def exitAlterByForce(self, ctx:SpeakQlParser.AlterByForceContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByValidate.
    def enterAlterByValidate(self, ctx:SpeakQlParser.AlterByValidateContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByValidate.
    def exitAlterByValidate(self, ctx:SpeakQlParser.AlterByValidateContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByAddPartition.
    def enterAlterByAddPartition(self, ctx:SpeakQlParser.AlterByAddPartitionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByAddPartition.
    def exitAlterByAddPartition(self, ctx:SpeakQlParser.AlterByAddPartitionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByDropPartition.
    def enterAlterByDropPartition(self, ctx:SpeakQlParser.AlterByDropPartitionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByDropPartition.
    def exitAlterByDropPartition(self, ctx:SpeakQlParser.AlterByDropPartitionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByDiscardPartition.
    def enterAlterByDiscardPartition(self, ctx:SpeakQlParser.AlterByDiscardPartitionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByDiscardPartition.
    def exitAlterByDiscardPartition(self, ctx:SpeakQlParser.AlterByDiscardPartitionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByImportPartition.
    def enterAlterByImportPartition(self, ctx:SpeakQlParser.AlterByImportPartitionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByImportPartition.
    def exitAlterByImportPartition(self, ctx:SpeakQlParser.AlterByImportPartitionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByTruncatePartition.
    def enterAlterByTruncatePartition(self, ctx:SpeakQlParser.AlterByTruncatePartitionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByTruncatePartition.
    def exitAlterByTruncatePartition(self, ctx:SpeakQlParser.AlterByTruncatePartitionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByCoalescePartition.
    def enterAlterByCoalescePartition(self, ctx:SpeakQlParser.AlterByCoalescePartitionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByCoalescePartition.
    def exitAlterByCoalescePartition(self, ctx:SpeakQlParser.AlterByCoalescePartitionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByReorganizePartition.
    def enterAlterByReorganizePartition(self, ctx:SpeakQlParser.AlterByReorganizePartitionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByReorganizePartition.
    def exitAlterByReorganizePartition(self, ctx:SpeakQlParser.AlterByReorganizePartitionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByExchangePartition.
    def enterAlterByExchangePartition(self, ctx:SpeakQlParser.AlterByExchangePartitionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByExchangePartition.
    def exitAlterByExchangePartition(self, ctx:SpeakQlParser.AlterByExchangePartitionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByAnalyzePartition.
    def enterAlterByAnalyzePartition(self, ctx:SpeakQlParser.AlterByAnalyzePartitionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByAnalyzePartition.
    def exitAlterByAnalyzePartition(self, ctx:SpeakQlParser.AlterByAnalyzePartitionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByCheckPartition.
    def enterAlterByCheckPartition(self, ctx:SpeakQlParser.AlterByCheckPartitionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByCheckPartition.
    def exitAlterByCheckPartition(self, ctx:SpeakQlParser.AlterByCheckPartitionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByOptimizePartition.
    def enterAlterByOptimizePartition(self, ctx:SpeakQlParser.AlterByOptimizePartitionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByOptimizePartition.
    def exitAlterByOptimizePartition(self, ctx:SpeakQlParser.AlterByOptimizePartitionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByRebuildPartition.
    def enterAlterByRebuildPartition(self, ctx:SpeakQlParser.AlterByRebuildPartitionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByRebuildPartition.
    def exitAlterByRebuildPartition(self, ctx:SpeakQlParser.AlterByRebuildPartitionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByRepairPartition.
    def enterAlterByRepairPartition(self, ctx:SpeakQlParser.AlterByRepairPartitionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByRepairPartition.
    def exitAlterByRepairPartition(self, ctx:SpeakQlParser.AlterByRepairPartitionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByRemovePartitioning.
    def enterAlterByRemovePartitioning(self, ctx:SpeakQlParser.AlterByRemovePartitioningContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByRemovePartitioning.
    def exitAlterByRemovePartitioning(self, ctx:SpeakQlParser.AlterByRemovePartitioningContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterByUpgradePartitioning.
    def enterAlterByUpgradePartitioning(self, ctx:SpeakQlParser.AlterByUpgradePartitioningContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterByUpgradePartitioning.
    def exitAlterByUpgradePartitioning(self, ctx:SpeakQlParser.AlterByUpgradePartitioningContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#dropDatabase.
    def enterDropDatabase(self, ctx:SpeakQlParser.DropDatabaseContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#dropDatabase.
    def exitDropDatabase(self, ctx:SpeakQlParser.DropDatabaseContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#dropEvent.
    def enterDropEvent(self, ctx:SpeakQlParser.DropEventContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#dropEvent.
    def exitDropEvent(self, ctx:SpeakQlParser.DropEventContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#dropIndex.
    def enterDropIndex(self, ctx:SpeakQlParser.DropIndexContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#dropIndex.
    def exitDropIndex(self, ctx:SpeakQlParser.DropIndexContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#dropLogfileGroup.
    def enterDropLogfileGroup(self, ctx:SpeakQlParser.DropLogfileGroupContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#dropLogfileGroup.
    def exitDropLogfileGroup(self, ctx:SpeakQlParser.DropLogfileGroupContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#dropProcedure.
    def enterDropProcedure(self, ctx:SpeakQlParser.DropProcedureContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#dropProcedure.
    def exitDropProcedure(self, ctx:SpeakQlParser.DropProcedureContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#dropFunction.
    def enterDropFunction(self, ctx:SpeakQlParser.DropFunctionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#dropFunction.
    def exitDropFunction(self, ctx:SpeakQlParser.DropFunctionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#dropServer.
    def enterDropServer(self, ctx:SpeakQlParser.DropServerContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#dropServer.
    def exitDropServer(self, ctx:SpeakQlParser.DropServerContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#dropTable.
    def enterDropTable(self, ctx:SpeakQlParser.DropTableContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#dropTable.
    def exitDropTable(self, ctx:SpeakQlParser.DropTableContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#dropTablespace.
    def enterDropTablespace(self, ctx:SpeakQlParser.DropTablespaceContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#dropTablespace.
    def exitDropTablespace(self, ctx:SpeakQlParser.DropTablespaceContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#dropTrigger.
    def enterDropTrigger(self, ctx:SpeakQlParser.DropTriggerContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#dropTrigger.
    def exitDropTrigger(self, ctx:SpeakQlParser.DropTriggerContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#dropView.
    def enterDropView(self, ctx:SpeakQlParser.DropViewContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#dropView.
    def exitDropView(self, ctx:SpeakQlParser.DropViewContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#renameTable.
    def enterRenameTable(self, ctx:SpeakQlParser.RenameTableContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#renameTable.
    def exitRenameTable(self, ctx:SpeakQlParser.RenameTableContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#renameTableClause.
    def enterRenameTableClause(self, ctx:SpeakQlParser.RenameTableClauseContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#renameTableClause.
    def exitRenameTableClause(self, ctx:SpeakQlParser.RenameTableClauseContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#truncateTable.
    def enterTruncateTable(self, ctx:SpeakQlParser.TruncateTableContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#truncateTable.
    def exitTruncateTable(self, ctx:SpeakQlParser.TruncateTableContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#callStatement.
    def enterCallStatement(self, ctx:SpeakQlParser.CallStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#callStatement.
    def exitCallStatement(self, ctx:SpeakQlParser.CallStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#deleteStatement.
    def enterDeleteStatement(self, ctx:SpeakQlParser.DeleteStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#deleteStatement.
    def exitDeleteStatement(self, ctx:SpeakQlParser.DeleteStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#doStatement.
    def enterDoStatement(self, ctx:SpeakQlParser.DoStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#doStatement.
    def exitDoStatement(self, ctx:SpeakQlParser.DoStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#handlerStatement.
    def enterHandlerStatement(self, ctx:SpeakQlParser.HandlerStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#handlerStatement.
    def exitHandlerStatement(self, ctx:SpeakQlParser.HandlerStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#insertStatement.
    def enterInsertStatement(self, ctx:SpeakQlParser.InsertStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#insertStatement.
    def exitInsertStatement(self, ctx:SpeakQlParser.InsertStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#loadDataStatement.
    def enterLoadDataStatement(self, ctx:SpeakQlParser.LoadDataStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#loadDataStatement.
    def exitLoadDataStatement(self, ctx:SpeakQlParser.LoadDataStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#loadXmlStatement.
    def enterLoadXmlStatement(self, ctx:SpeakQlParser.LoadXmlStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#loadXmlStatement.
    def exitLoadXmlStatement(self, ctx:SpeakQlParser.LoadXmlStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#replaceStatement.
    def enterReplaceStatement(self, ctx:SpeakQlParser.ReplaceStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#replaceStatement.
    def exitReplaceStatement(self, ctx:SpeakQlParser.ReplaceStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#simpleSelect.
    def enterSimpleSelect(self, ctx:SpeakQlParser.SimpleSelectContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#simpleSelect.
    def exitSimpleSelect(self, ctx:SpeakQlParser.SimpleSelectContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#parenthesisSelect.
    def enterParenthesisSelect(self, ctx:SpeakQlParser.ParenthesisSelectContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#parenthesisSelect.
    def exitParenthesisSelect(self, ctx:SpeakQlParser.ParenthesisSelectContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#unionSelect.
    def enterUnionSelect(self, ctx:SpeakQlParser.UnionSelectContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#unionSelect.
    def exitUnionSelect(self, ctx:SpeakQlParser.UnionSelectContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#unionParenthesisSelect.
    def enterUnionParenthesisSelect(self, ctx:SpeakQlParser.UnionParenthesisSelectContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#unionParenthesisSelect.
    def exitUnionParenthesisSelect(self, ctx:SpeakQlParser.UnionParenthesisSelectContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#updateStatement.
    def enterUpdateStatement(self, ctx:SpeakQlParser.UpdateStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#updateStatement.
    def exitUpdateStatement(self, ctx:SpeakQlParser.UpdateStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#insertStatementValue.
    def enterInsertStatementValue(self, ctx:SpeakQlParser.InsertStatementValueContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#insertStatementValue.
    def exitInsertStatementValue(self, ctx:SpeakQlParser.InsertStatementValueContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#updatedElement.
    def enterUpdatedElement(self, ctx:SpeakQlParser.UpdatedElementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#updatedElement.
    def exitUpdatedElement(self, ctx:SpeakQlParser.UpdatedElementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#assignmentField.
    def enterAssignmentField(self, ctx:SpeakQlParser.AssignmentFieldContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#assignmentField.
    def exitAssignmentField(self, ctx:SpeakQlParser.AssignmentFieldContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#lockClause.
    def enterLockClause(self, ctx:SpeakQlParser.LockClauseContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#lockClause.
    def exitLockClause(self, ctx:SpeakQlParser.LockClauseContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#singleDeleteStatement.
    def enterSingleDeleteStatement(self, ctx:SpeakQlParser.SingleDeleteStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#singleDeleteStatement.
    def exitSingleDeleteStatement(self, ctx:SpeakQlParser.SingleDeleteStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#multipleDeleteStatement.
    def enterMultipleDeleteStatement(self, ctx:SpeakQlParser.MultipleDeleteStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#multipleDeleteStatement.
    def exitMultipleDeleteStatement(self, ctx:SpeakQlParser.MultipleDeleteStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#handlerOpenStatement.
    def enterHandlerOpenStatement(self, ctx:SpeakQlParser.HandlerOpenStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#handlerOpenStatement.
    def exitHandlerOpenStatement(self, ctx:SpeakQlParser.HandlerOpenStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#handlerReadIndexStatement.
    def enterHandlerReadIndexStatement(self, ctx:SpeakQlParser.HandlerReadIndexStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#handlerReadIndexStatement.
    def exitHandlerReadIndexStatement(self, ctx:SpeakQlParser.HandlerReadIndexStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#handlerReadStatement.
    def enterHandlerReadStatement(self, ctx:SpeakQlParser.HandlerReadStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#handlerReadStatement.
    def exitHandlerReadStatement(self, ctx:SpeakQlParser.HandlerReadStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#handlerCloseStatement.
    def enterHandlerCloseStatement(self, ctx:SpeakQlParser.HandlerCloseStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#handlerCloseStatement.
    def exitHandlerCloseStatement(self, ctx:SpeakQlParser.HandlerCloseStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#singleUpdateStatement.
    def enterSingleUpdateStatement(self, ctx:SpeakQlParser.SingleUpdateStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#singleUpdateStatement.
    def exitSingleUpdateStatement(self, ctx:SpeakQlParser.SingleUpdateStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#multipleUpdateStatement.
    def enterMultipleUpdateStatement(self, ctx:SpeakQlParser.MultipleUpdateStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#multipleUpdateStatement.
    def exitMultipleUpdateStatement(self, ctx:SpeakQlParser.MultipleUpdateStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#orderByClause.
    def enterOrderByClause(self, ctx:SpeakQlParser.OrderByClauseContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#orderByClause.
    def exitOrderByClause(self, ctx:SpeakQlParser.OrderByClauseContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#orderByExpression.
    def enterOrderByExpression(self, ctx:SpeakQlParser.OrderByExpressionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#orderByExpression.
    def exitOrderByExpression(self, ctx:SpeakQlParser.OrderByExpressionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableSources.
    def enterTableSources(self, ctx:SpeakQlParser.TableSourcesContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableSources.
    def exitTableSources(self, ctx:SpeakQlParser.TableSourcesContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableSourceBase.
    def enterTableSourceBase(self, ctx:SpeakQlParser.TableSourceBaseContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableSourceBase.
    def exitTableSourceBase(self, ctx:SpeakQlParser.TableSourceBaseContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableSourceNested.
    def enterTableSourceNested(self, ctx:SpeakQlParser.TableSourceNestedContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableSourceNested.
    def exitTableSourceNested(self, ctx:SpeakQlParser.TableSourceNestedContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#atomTableItem.
    def enterAtomTableItem(self, ctx:SpeakQlParser.AtomTableItemContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#atomTableItem.
    def exitAtomTableItem(self, ctx:SpeakQlParser.AtomTableItemContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#subqueryTableItem.
    def enterSubqueryTableItem(self, ctx:SpeakQlParser.SubqueryTableItemContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#subqueryTableItem.
    def exitSubqueryTableItem(self, ctx:SpeakQlParser.SubqueryTableItemContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableSourcesItem.
    def enterTableSourcesItem(self, ctx:SpeakQlParser.TableSourcesItemContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableSourcesItem.
    def exitTableSourcesItem(self, ctx:SpeakQlParser.TableSourcesItemContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#indexHint.
    def enterIndexHint(self, ctx:SpeakQlParser.IndexHintContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#indexHint.
    def exitIndexHint(self, ctx:SpeakQlParser.IndexHintContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#indexHintType.
    def enterIndexHintType(self, ctx:SpeakQlParser.IndexHintTypeContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#indexHintType.
    def exitIndexHintType(self, ctx:SpeakQlParser.IndexHintTypeContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#innerJoin.
    def enterInnerJoin(self, ctx:SpeakQlParser.InnerJoinContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#innerJoin.
    def exitInnerJoin(self, ctx:SpeakQlParser.InnerJoinContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#straightJoin.
    def enterStraightJoin(self, ctx:SpeakQlParser.StraightJoinContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#straightJoin.
    def exitStraightJoin(self, ctx:SpeakQlParser.StraightJoinContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#outerJoin.
    def enterOuterJoin(self, ctx:SpeakQlParser.OuterJoinContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#outerJoin.
    def exitOuterJoin(self, ctx:SpeakQlParser.OuterJoinContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#naturalJoin.
    def enterNaturalJoin(self, ctx:SpeakQlParser.NaturalJoinContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#naturalJoin.
    def exitNaturalJoin(self, ctx:SpeakQlParser.NaturalJoinContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#joinKeyword.
    def enterJoinKeyword(self, ctx:SpeakQlParser.JoinKeywordContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#joinKeyword.
    def exitJoinKeyword(self, ctx:SpeakQlParser.JoinKeywordContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#queryExpression.
    def enterQueryExpression(self, ctx:SpeakQlParser.QueryExpressionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#queryExpression.
    def exitQueryExpression(self, ctx:SpeakQlParser.QueryExpressionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#queryExpressionNointo.
    def enterQueryExpressionNointo(self, ctx:SpeakQlParser.QueryExpressionNointoContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#queryExpressionNointo.
    def exitQueryExpressionNointo(self, ctx:SpeakQlParser.QueryExpressionNointoContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#querySpecification.
    def enterQuerySpecification(self, ctx:SpeakQlParser.QuerySpecificationContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#querySpecification.
    def exitQuerySpecification(self, ctx:SpeakQlParser.QuerySpecificationContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#selectModifierExpression.
    def enterSelectModifierExpression(self, ctx:SpeakQlParser.SelectModifierExpressionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#selectModifierExpression.
    def exitSelectModifierExpression(self, ctx:SpeakQlParser.SelectModifierExpressionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#selectExpression.
    def enterSelectExpression(self, ctx:SpeakQlParser.SelectExpressionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#selectExpression.
    def exitSelectExpression(self, ctx:SpeakQlParser.SelectExpressionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableExpression.
    def enterTableExpression(self, ctx:SpeakQlParser.TableExpressionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableExpression.
    def exitTableExpression(self, ctx:SpeakQlParser.TableExpressionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#selectClause.
    def enterSelectClause(self, ctx:SpeakQlParser.SelectClauseContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#selectClause.
    def exitSelectClause(self, ctx:SpeakQlParser.SelectClauseContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#selectKeyword.
    def enterSelectKeyword(self, ctx:SpeakQlParser.SelectKeywordContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#selectKeyword.
    def exitSelectKeyword(self, ctx:SpeakQlParser.SelectKeywordContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#querySpecificationNointo.
    def enterQuerySpecificationNointo(self, ctx:SpeakQlParser.QuerySpecificationNointoContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#querySpecificationNointo.
    def exitQuerySpecificationNointo(self, ctx:SpeakQlParser.QuerySpecificationNointoContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#unionParenthesis.
    def enterUnionParenthesis(self, ctx:SpeakQlParser.UnionParenthesisContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#unionParenthesis.
    def exitUnionParenthesis(self, ctx:SpeakQlParser.UnionParenthesisContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#unionStatement.
    def enterUnionStatement(self, ctx:SpeakQlParser.UnionStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#unionStatement.
    def exitUnionStatement(self, ctx:SpeakQlParser.UnionStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#selectSpec.
    def enterSelectSpec(self, ctx:SpeakQlParser.SelectSpecContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#selectSpec.
    def exitSelectSpec(self, ctx:SpeakQlParser.SelectSpecContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#selectElements.
    def enterSelectElements(self, ctx:SpeakQlParser.SelectElementsContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#selectElements.
    def exitSelectElements(self, ctx:SpeakQlParser.SelectElementsContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#selectElementDelimiter.
    def enterSelectElementDelimiter(self, ctx:SpeakQlParser.SelectElementDelimiterContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#selectElementDelimiter.
    def exitSelectElementDelimiter(self, ctx:SpeakQlParser.SelectElementDelimiterContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#selectStarElement.
    def enterSelectStarElement(self, ctx:SpeakQlParser.SelectStarElementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#selectStarElement.
    def exitSelectStarElement(self, ctx:SpeakQlParser.SelectStarElementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#selectColumnElement.
    def enterSelectColumnElement(self, ctx:SpeakQlParser.SelectColumnElementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#selectColumnElement.
    def exitSelectColumnElement(self, ctx:SpeakQlParser.SelectColumnElementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#selectFunctionElement.
    def enterSelectFunctionElement(self, ctx:SpeakQlParser.SelectFunctionElementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#selectFunctionElement.
    def exitSelectFunctionElement(self, ctx:SpeakQlParser.SelectFunctionElementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#selectExpressionElement.
    def enterSelectExpressionElement(self, ctx:SpeakQlParser.SelectExpressionElementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#selectExpressionElement.
    def exitSelectExpressionElement(self, ctx:SpeakQlParser.SelectExpressionElementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#selectIntoVariables.
    def enterSelectIntoVariables(self, ctx:SpeakQlParser.SelectIntoVariablesContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#selectIntoVariables.
    def exitSelectIntoVariables(self, ctx:SpeakQlParser.SelectIntoVariablesContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#selectIntoDumpFile.
    def enterSelectIntoDumpFile(self, ctx:SpeakQlParser.SelectIntoDumpFileContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#selectIntoDumpFile.
    def exitSelectIntoDumpFile(self, ctx:SpeakQlParser.SelectIntoDumpFileContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#selectIntoTextFile.
    def enterSelectIntoTextFile(self, ctx:SpeakQlParser.SelectIntoTextFileContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#selectIntoTextFile.
    def exitSelectIntoTextFile(self, ctx:SpeakQlParser.SelectIntoTextFileContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#selectFieldsInto.
    def enterSelectFieldsInto(self, ctx:SpeakQlParser.SelectFieldsIntoContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#selectFieldsInto.
    def exitSelectFieldsInto(self, ctx:SpeakQlParser.SelectFieldsIntoContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#selectLinesInto.
    def enterSelectLinesInto(self, ctx:SpeakQlParser.SelectLinesIntoContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#selectLinesInto.
    def exitSelectLinesInto(self, ctx:SpeakQlParser.SelectLinesIntoContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#fromClause.
    def enterFromClause(self, ctx:SpeakQlParser.FromClauseContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#fromClause.
    def exitFromClause(self, ctx:SpeakQlParser.FromClauseContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#fromKeyword.
    def enterFromKeyword(self, ctx:SpeakQlParser.FromKeywordContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#fromKeyword.
    def exitFromKeyword(self, ctx:SpeakQlParser.FromKeywordContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#groupByClause.
    def enterGroupByClause(self, ctx:SpeakQlParser.GroupByClauseContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#groupByClause.
    def exitGroupByClause(self, ctx:SpeakQlParser.GroupByClauseContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#havingClause.
    def enterHavingClause(self, ctx:SpeakQlParser.HavingClauseContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#havingClause.
    def exitHavingClause(self, ctx:SpeakQlParser.HavingClauseContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#windowClause.
    def enterWindowClause(self, ctx:SpeakQlParser.WindowClauseContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#windowClause.
    def exitWindowClause(self, ctx:SpeakQlParser.WindowClauseContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#groupByItem.
    def enterGroupByItem(self, ctx:SpeakQlParser.GroupByItemContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#groupByItem.
    def exitGroupByItem(self, ctx:SpeakQlParser.GroupByItemContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#limitClause.
    def enterLimitClause(self, ctx:SpeakQlParser.LimitClauseContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#limitClause.
    def exitLimitClause(self, ctx:SpeakQlParser.LimitClauseContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#limitClauseAtom.
    def enterLimitClauseAtom(self, ctx:SpeakQlParser.LimitClauseAtomContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#limitClauseAtom.
    def exitLimitClauseAtom(self, ctx:SpeakQlParser.LimitClauseAtomContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#startTransaction.
    def enterStartTransaction(self, ctx:SpeakQlParser.StartTransactionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#startTransaction.
    def exitStartTransaction(self, ctx:SpeakQlParser.StartTransactionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#beginWork.
    def enterBeginWork(self, ctx:SpeakQlParser.BeginWorkContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#beginWork.
    def exitBeginWork(self, ctx:SpeakQlParser.BeginWorkContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#commitWork.
    def enterCommitWork(self, ctx:SpeakQlParser.CommitWorkContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#commitWork.
    def exitCommitWork(self, ctx:SpeakQlParser.CommitWorkContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#rollbackWork.
    def enterRollbackWork(self, ctx:SpeakQlParser.RollbackWorkContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#rollbackWork.
    def exitRollbackWork(self, ctx:SpeakQlParser.RollbackWorkContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#savepointStatement.
    def enterSavepointStatement(self, ctx:SpeakQlParser.SavepointStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#savepointStatement.
    def exitSavepointStatement(self, ctx:SpeakQlParser.SavepointStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#rollbackStatement.
    def enterRollbackStatement(self, ctx:SpeakQlParser.RollbackStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#rollbackStatement.
    def exitRollbackStatement(self, ctx:SpeakQlParser.RollbackStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#releaseStatement.
    def enterReleaseStatement(self, ctx:SpeakQlParser.ReleaseStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#releaseStatement.
    def exitReleaseStatement(self, ctx:SpeakQlParser.ReleaseStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#lockTables.
    def enterLockTables(self, ctx:SpeakQlParser.LockTablesContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#lockTables.
    def exitLockTables(self, ctx:SpeakQlParser.LockTablesContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#unlockTables.
    def enterUnlockTables(self, ctx:SpeakQlParser.UnlockTablesContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#unlockTables.
    def exitUnlockTables(self, ctx:SpeakQlParser.UnlockTablesContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#setAutocommitStatement.
    def enterSetAutocommitStatement(self, ctx:SpeakQlParser.SetAutocommitStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#setAutocommitStatement.
    def exitSetAutocommitStatement(self, ctx:SpeakQlParser.SetAutocommitStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#setTransactionStatement.
    def enterSetTransactionStatement(self, ctx:SpeakQlParser.SetTransactionStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#setTransactionStatement.
    def exitSetTransactionStatement(self, ctx:SpeakQlParser.SetTransactionStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#transactionMode.
    def enterTransactionMode(self, ctx:SpeakQlParser.TransactionModeContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#transactionMode.
    def exitTransactionMode(self, ctx:SpeakQlParser.TransactionModeContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#lockTableElement.
    def enterLockTableElement(self, ctx:SpeakQlParser.LockTableElementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#lockTableElement.
    def exitLockTableElement(self, ctx:SpeakQlParser.LockTableElementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#lockAction.
    def enterLockAction(self, ctx:SpeakQlParser.LockActionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#lockAction.
    def exitLockAction(self, ctx:SpeakQlParser.LockActionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#transactionOption.
    def enterTransactionOption(self, ctx:SpeakQlParser.TransactionOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#transactionOption.
    def exitTransactionOption(self, ctx:SpeakQlParser.TransactionOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#transactionLevel.
    def enterTransactionLevel(self, ctx:SpeakQlParser.TransactionLevelContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#transactionLevel.
    def exitTransactionLevel(self, ctx:SpeakQlParser.TransactionLevelContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#changeMaster.
    def enterChangeMaster(self, ctx:SpeakQlParser.ChangeMasterContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#changeMaster.
    def exitChangeMaster(self, ctx:SpeakQlParser.ChangeMasterContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#changeReplicationFilter.
    def enterChangeReplicationFilter(self, ctx:SpeakQlParser.ChangeReplicationFilterContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#changeReplicationFilter.
    def exitChangeReplicationFilter(self, ctx:SpeakQlParser.ChangeReplicationFilterContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#purgeBinaryLogs.
    def enterPurgeBinaryLogs(self, ctx:SpeakQlParser.PurgeBinaryLogsContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#purgeBinaryLogs.
    def exitPurgeBinaryLogs(self, ctx:SpeakQlParser.PurgeBinaryLogsContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#resetMaster.
    def enterResetMaster(self, ctx:SpeakQlParser.ResetMasterContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#resetMaster.
    def exitResetMaster(self, ctx:SpeakQlParser.ResetMasterContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#resetSlave.
    def enterResetSlave(self, ctx:SpeakQlParser.ResetSlaveContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#resetSlave.
    def exitResetSlave(self, ctx:SpeakQlParser.ResetSlaveContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#startSlave.
    def enterStartSlave(self, ctx:SpeakQlParser.StartSlaveContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#startSlave.
    def exitStartSlave(self, ctx:SpeakQlParser.StartSlaveContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#stopSlave.
    def enterStopSlave(self, ctx:SpeakQlParser.StopSlaveContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#stopSlave.
    def exitStopSlave(self, ctx:SpeakQlParser.StopSlaveContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#startGroupReplication.
    def enterStartGroupReplication(self, ctx:SpeakQlParser.StartGroupReplicationContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#startGroupReplication.
    def exitStartGroupReplication(self, ctx:SpeakQlParser.StartGroupReplicationContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#stopGroupReplication.
    def enterStopGroupReplication(self, ctx:SpeakQlParser.StopGroupReplicationContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#stopGroupReplication.
    def exitStopGroupReplication(self, ctx:SpeakQlParser.StopGroupReplicationContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#masterStringOption.
    def enterMasterStringOption(self, ctx:SpeakQlParser.MasterStringOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#masterStringOption.
    def exitMasterStringOption(self, ctx:SpeakQlParser.MasterStringOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#masterDecimalOption.
    def enterMasterDecimalOption(self, ctx:SpeakQlParser.MasterDecimalOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#masterDecimalOption.
    def exitMasterDecimalOption(self, ctx:SpeakQlParser.MasterDecimalOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#masterBoolOption.
    def enterMasterBoolOption(self, ctx:SpeakQlParser.MasterBoolOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#masterBoolOption.
    def exitMasterBoolOption(self, ctx:SpeakQlParser.MasterBoolOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#masterRealOption.
    def enterMasterRealOption(self, ctx:SpeakQlParser.MasterRealOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#masterRealOption.
    def exitMasterRealOption(self, ctx:SpeakQlParser.MasterRealOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#masterUidListOption.
    def enterMasterUidListOption(self, ctx:SpeakQlParser.MasterUidListOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#masterUidListOption.
    def exitMasterUidListOption(self, ctx:SpeakQlParser.MasterUidListOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#stringMasterOption.
    def enterStringMasterOption(self, ctx:SpeakQlParser.StringMasterOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#stringMasterOption.
    def exitStringMasterOption(self, ctx:SpeakQlParser.StringMasterOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#decimalMasterOption.
    def enterDecimalMasterOption(self, ctx:SpeakQlParser.DecimalMasterOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#decimalMasterOption.
    def exitDecimalMasterOption(self, ctx:SpeakQlParser.DecimalMasterOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#boolMasterOption.
    def enterBoolMasterOption(self, ctx:SpeakQlParser.BoolMasterOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#boolMasterOption.
    def exitBoolMasterOption(self, ctx:SpeakQlParser.BoolMasterOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#channelOption.
    def enterChannelOption(self, ctx:SpeakQlParser.ChannelOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#channelOption.
    def exitChannelOption(self, ctx:SpeakQlParser.ChannelOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#doDbReplication.
    def enterDoDbReplication(self, ctx:SpeakQlParser.DoDbReplicationContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#doDbReplication.
    def exitDoDbReplication(self, ctx:SpeakQlParser.DoDbReplicationContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#ignoreDbReplication.
    def enterIgnoreDbReplication(self, ctx:SpeakQlParser.IgnoreDbReplicationContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#ignoreDbReplication.
    def exitIgnoreDbReplication(self, ctx:SpeakQlParser.IgnoreDbReplicationContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#doTableReplication.
    def enterDoTableReplication(self, ctx:SpeakQlParser.DoTableReplicationContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#doTableReplication.
    def exitDoTableReplication(self, ctx:SpeakQlParser.DoTableReplicationContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#ignoreTableReplication.
    def enterIgnoreTableReplication(self, ctx:SpeakQlParser.IgnoreTableReplicationContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#ignoreTableReplication.
    def exitIgnoreTableReplication(self, ctx:SpeakQlParser.IgnoreTableReplicationContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#wildDoTableReplication.
    def enterWildDoTableReplication(self, ctx:SpeakQlParser.WildDoTableReplicationContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#wildDoTableReplication.
    def exitWildDoTableReplication(self, ctx:SpeakQlParser.WildDoTableReplicationContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#wildIgnoreTableReplication.
    def enterWildIgnoreTableReplication(self, ctx:SpeakQlParser.WildIgnoreTableReplicationContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#wildIgnoreTableReplication.
    def exitWildIgnoreTableReplication(self, ctx:SpeakQlParser.WildIgnoreTableReplicationContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#rewriteDbReplication.
    def enterRewriteDbReplication(self, ctx:SpeakQlParser.RewriteDbReplicationContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#rewriteDbReplication.
    def exitRewriteDbReplication(self, ctx:SpeakQlParser.RewriteDbReplicationContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tablePair.
    def enterTablePair(self, ctx:SpeakQlParser.TablePairContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tablePair.
    def exitTablePair(self, ctx:SpeakQlParser.TablePairContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#threadType.
    def enterThreadType(self, ctx:SpeakQlParser.ThreadTypeContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#threadType.
    def exitThreadType(self, ctx:SpeakQlParser.ThreadTypeContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#gtidsUntilOption.
    def enterGtidsUntilOption(self, ctx:SpeakQlParser.GtidsUntilOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#gtidsUntilOption.
    def exitGtidsUntilOption(self, ctx:SpeakQlParser.GtidsUntilOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#masterLogUntilOption.
    def enterMasterLogUntilOption(self, ctx:SpeakQlParser.MasterLogUntilOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#masterLogUntilOption.
    def exitMasterLogUntilOption(self, ctx:SpeakQlParser.MasterLogUntilOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#relayLogUntilOption.
    def enterRelayLogUntilOption(self, ctx:SpeakQlParser.RelayLogUntilOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#relayLogUntilOption.
    def exitRelayLogUntilOption(self, ctx:SpeakQlParser.RelayLogUntilOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#sqlGapsUntilOption.
    def enterSqlGapsUntilOption(self, ctx:SpeakQlParser.SqlGapsUntilOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#sqlGapsUntilOption.
    def exitSqlGapsUntilOption(self, ctx:SpeakQlParser.SqlGapsUntilOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#userConnectionOption.
    def enterUserConnectionOption(self, ctx:SpeakQlParser.UserConnectionOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#userConnectionOption.
    def exitUserConnectionOption(self, ctx:SpeakQlParser.UserConnectionOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#passwordConnectionOption.
    def enterPasswordConnectionOption(self, ctx:SpeakQlParser.PasswordConnectionOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#passwordConnectionOption.
    def exitPasswordConnectionOption(self, ctx:SpeakQlParser.PasswordConnectionOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#defaultAuthConnectionOption.
    def enterDefaultAuthConnectionOption(self, ctx:SpeakQlParser.DefaultAuthConnectionOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#defaultAuthConnectionOption.
    def exitDefaultAuthConnectionOption(self, ctx:SpeakQlParser.DefaultAuthConnectionOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#pluginDirConnectionOption.
    def enterPluginDirConnectionOption(self, ctx:SpeakQlParser.PluginDirConnectionOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#pluginDirConnectionOption.
    def exitPluginDirConnectionOption(self, ctx:SpeakQlParser.PluginDirConnectionOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#gtuidSet.
    def enterGtuidSet(self, ctx:SpeakQlParser.GtuidSetContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#gtuidSet.
    def exitGtuidSet(self, ctx:SpeakQlParser.GtuidSetContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#xaStartTransaction.
    def enterXaStartTransaction(self, ctx:SpeakQlParser.XaStartTransactionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#xaStartTransaction.
    def exitXaStartTransaction(self, ctx:SpeakQlParser.XaStartTransactionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#xaEndTransaction.
    def enterXaEndTransaction(self, ctx:SpeakQlParser.XaEndTransactionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#xaEndTransaction.
    def exitXaEndTransaction(self, ctx:SpeakQlParser.XaEndTransactionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#xaPrepareStatement.
    def enterXaPrepareStatement(self, ctx:SpeakQlParser.XaPrepareStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#xaPrepareStatement.
    def exitXaPrepareStatement(self, ctx:SpeakQlParser.XaPrepareStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#xaCommitWork.
    def enterXaCommitWork(self, ctx:SpeakQlParser.XaCommitWorkContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#xaCommitWork.
    def exitXaCommitWork(self, ctx:SpeakQlParser.XaCommitWorkContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#xaRollbackWork.
    def enterXaRollbackWork(self, ctx:SpeakQlParser.XaRollbackWorkContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#xaRollbackWork.
    def exitXaRollbackWork(self, ctx:SpeakQlParser.XaRollbackWorkContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#xaRecoverWork.
    def enterXaRecoverWork(self, ctx:SpeakQlParser.XaRecoverWorkContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#xaRecoverWork.
    def exitXaRecoverWork(self, ctx:SpeakQlParser.XaRecoverWorkContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#prepareStatement.
    def enterPrepareStatement(self, ctx:SpeakQlParser.PrepareStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#prepareStatement.
    def exitPrepareStatement(self, ctx:SpeakQlParser.PrepareStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#executeStatement.
    def enterExecuteStatement(self, ctx:SpeakQlParser.ExecuteStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#executeStatement.
    def exitExecuteStatement(self, ctx:SpeakQlParser.ExecuteStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#deallocatePrepare.
    def enterDeallocatePrepare(self, ctx:SpeakQlParser.DeallocatePrepareContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#deallocatePrepare.
    def exitDeallocatePrepare(self, ctx:SpeakQlParser.DeallocatePrepareContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#routineBody.
    def enterRoutineBody(self, ctx:SpeakQlParser.RoutineBodyContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#routineBody.
    def exitRoutineBody(self, ctx:SpeakQlParser.RoutineBodyContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#blockStatement.
    def enterBlockStatement(self, ctx:SpeakQlParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#blockStatement.
    def exitBlockStatement(self, ctx:SpeakQlParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#caseStatement.
    def enterCaseStatement(self, ctx:SpeakQlParser.CaseStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#caseStatement.
    def exitCaseStatement(self, ctx:SpeakQlParser.CaseStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#ifStatement.
    def enterIfStatement(self, ctx:SpeakQlParser.IfStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#ifStatement.
    def exitIfStatement(self, ctx:SpeakQlParser.IfStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#iterateStatement.
    def enterIterateStatement(self, ctx:SpeakQlParser.IterateStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#iterateStatement.
    def exitIterateStatement(self, ctx:SpeakQlParser.IterateStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#leaveStatement.
    def enterLeaveStatement(self, ctx:SpeakQlParser.LeaveStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#leaveStatement.
    def exitLeaveStatement(self, ctx:SpeakQlParser.LeaveStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#loopStatement.
    def enterLoopStatement(self, ctx:SpeakQlParser.LoopStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#loopStatement.
    def exitLoopStatement(self, ctx:SpeakQlParser.LoopStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#repeatStatement.
    def enterRepeatStatement(self, ctx:SpeakQlParser.RepeatStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#repeatStatement.
    def exitRepeatStatement(self, ctx:SpeakQlParser.RepeatStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#returnStatement.
    def enterReturnStatement(self, ctx:SpeakQlParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#returnStatement.
    def exitReturnStatement(self, ctx:SpeakQlParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#whileStatement.
    def enterWhileStatement(self, ctx:SpeakQlParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#whileStatement.
    def exitWhileStatement(self, ctx:SpeakQlParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#CloseCursor.
    def enterCloseCursor(self, ctx:SpeakQlParser.CloseCursorContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#CloseCursor.
    def exitCloseCursor(self, ctx:SpeakQlParser.CloseCursorContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#FetchCursor.
    def enterFetchCursor(self, ctx:SpeakQlParser.FetchCursorContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#FetchCursor.
    def exitFetchCursor(self, ctx:SpeakQlParser.FetchCursorContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#OpenCursor.
    def enterOpenCursor(self, ctx:SpeakQlParser.OpenCursorContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#OpenCursor.
    def exitOpenCursor(self, ctx:SpeakQlParser.OpenCursorContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#declareVariable.
    def enterDeclareVariable(self, ctx:SpeakQlParser.DeclareVariableContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#declareVariable.
    def exitDeclareVariable(self, ctx:SpeakQlParser.DeclareVariableContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#declareCondition.
    def enterDeclareCondition(self, ctx:SpeakQlParser.DeclareConditionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#declareCondition.
    def exitDeclareCondition(self, ctx:SpeakQlParser.DeclareConditionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#declareCursor.
    def enterDeclareCursor(self, ctx:SpeakQlParser.DeclareCursorContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#declareCursor.
    def exitDeclareCursor(self, ctx:SpeakQlParser.DeclareCursorContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#declareHandler.
    def enterDeclareHandler(self, ctx:SpeakQlParser.DeclareHandlerContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#declareHandler.
    def exitDeclareHandler(self, ctx:SpeakQlParser.DeclareHandlerContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#handlerConditionCode.
    def enterHandlerConditionCode(self, ctx:SpeakQlParser.HandlerConditionCodeContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#handlerConditionCode.
    def exitHandlerConditionCode(self, ctx:SpeakQlParser.HandlerConditionCodeContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#handlerConditionState.
    def enterHandlerConditionState(self, ctx:SpeakQlParser.HandlerConditionStateContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#handlerConditionState.
    def exitHandlerConditionState(self, ctx:SpeakQlParser.HandlerConditionStateContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#handlerConditionName.
    def enterHandlerConditionName(self, ctx:SpeakQlParser.HandlerConditionNameContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#handlerConditionName.
    def exitHandlerConditionName(self, ctx:SpeakQlParser.HandlerConditionNameContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#handlerConditionWarning.
    def enterHandlerConditionWarning(self, ctx:SpeakQlParser.HandlerConditionWarningContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#handlerConditionWarning.
    def exitHandlerConditionWarning(self, ctx:SpeakQlParser.HandlerConditionWarningContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#handlerConditionNotfound.
    def enterHandlerConditionNotfound(self, ctx:SpeakQlParser.HandlerConditionNotfoundContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#handlerConditionNotfound.
    def exitHandlerConditionNotfound(self, ctx:SpeakQlParser.HandlerConditionNotfoundContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#handlerConditionException.
    def enterHandlerConditionException(self, ctx:SpeakQlParser.HandlerConditionExceptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#handlerConditionException.
    def exitHandlerConditionException(self, ctx:SpeakQlParser.HandlerConditionExceptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#procedureSqlStatement.
    def enterProcedureSqlStatement(self, ctx:SpeakQlParser.ProcedureSqlStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#procedureSqlStatement.
    def exitProcedureSqlStatement(self, ctx:SpeakQlParser.ProcedureSqlStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#caseAlternative.
    def enterCaseAlternative(self, ctx:SpeakQlParser.CaseAlternativeContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#caseAlternative.
    def exitCaseAlternative(self, ctx:SpeakQlParser.CaseAlternativeContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#elifAlternative.
    def enterElifAlternative(self, ctx:SpeakQlParser.ElifAlternativeContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#elifAlternative.
    def exitElifAlternative(self, ctx:SpeakQlParser.ElifAlternativeContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterUserMysqlV56.
    def enterAlterUserMysqlV56(self, ctx:SpeakQlParser.AlterUserMysqlV56Context):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterUserMysqlV56.
    def exitAlterUserMysqlV56(self, ctx:SpeakQlParser.AlterUserMysqlV56Context):
        pass


    # Enter a parse tree produced by SpeakQlParser#alterUserMysqlV57.
    def enterAlterUserMysqlV57(self, ctx:SpeakQlParser.AlterUserMysqlV57Context):
        pass

    # Exit a parse tree produced by SpeakQlParser#alterUserMysqlV57.
    def exitAlterUserMysqlV57(self, ctx:SpeakQlParser.AlterUserMysqlV57Context):
        pass


    # Enter a parse tree produced by SpeakQlParser#createUserMysqlV56.
    def enterCreateUserMysqlV56(self, ctx:SpeakQlParser.CreateUserMysqlV56Context):
        pass

    # Exit a parse tree produced by SpeakQlParser#createUserMysqlV56.
    def exitCreateUserMysqlV56(self, ctx:SpeakQlParser.CreateUserMysqlV56Context):
        pass


    # Enter a parse tree produced by SpeakQlParser#createUserMysqlV57.
    def enterCreateUserMysqlV57(self, ctx:SpeakQlParser.CreateUserMysqlV57Context):
        pass

    # Exit a parse tree produced by SpeakQlParser#createUserMysqlV57.
    def exitCreateUserMysqlV57(self, ctx:SpeakQlParser.CreateUserMysqlV57Context):
        pass


    # Enter a parse tree produced by SpeakQlParser#dropUser.
    def enterDropUser(self, ctx:SpeakQlParser.DropUserContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#dropUser.
    def exitDropUser(self, ctx:SpeakQlParser.DropUserContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#grantStatement.
    def enterGrantStatement(self, ctx:SpeakQlParser.GrantStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#grantStatement.
    def exitGrantStatement(self, ctx:SpeakQlParser.GrantStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#roleOption.
    def enterRoleOption(self, ctx:SpeakQlParser.RoleOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#roleOption.
    def exitRoleOption(self, ctx:SpeakQlParser.RoleOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#grantProxy.
    def enterGrantProxy(self, ctx:SpeakQlParser.GrantProxyContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#grantProxy.
    def exitGrantProxy(self, ctx:SpeakQlParser.GrantProxyContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#renameUser.
    def enterRenameUser(self, ctx:SpeakQlParser.RenameUserContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#renameUser.
    def exitRenameUser(self, ctx:SpeakQlParser.RenameUserContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#detailRevoke.
    def enterDetailRevoke(self, ctx:SpeakQlParser.DetailRevokeContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#detailRevoke.
    def exitDetailRevoke(self, ctx:SpeakQlParser.DetailRevokeContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#shortRevoke.
    def enterShortRevoke(self, ctx:SpeakQlParser.ShortRevokeContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#shortRevoke.
    def exitShortRevoke(self, ctx:SpeakQlParser.ShortRevokeContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#roleRevoke.
    def enterRoleRevoke(self, ctx:SpeakQlParser.RoleRevokeContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#roleRevoke.
    def exitRoleRevoke(self, ctx:SpeakQlParser.RoleRevokeContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#revokeProxy.
    def enterRevokeProxy(self, ctx:SpeakQlParser.RevokeProxyContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#revokeProxy.
    def exitRevokeProxy(self, ctx:SpeakQlParser.RevokeProxyContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#setPasswordStatement.
    def enterSetPasswordStatement(self, ctx:SpeakQlParser.SetPasswordStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#setPasswordStatement.
    def exitSetPasswordStatement(self, ctx:SpeakQlParser.SetPasswordStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#userSpecification.
    def enterUserSpecification(self, ctx:SpeakQlParser.UserSpecificationContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#userSpecification.
    def exitUserSpecification(self, ctx:SpeakQlParser.UserSpecificationContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#passwordAuthOption.
    def enterPasswordAuthOption(self, ctx:SpeakQlParser.PasswordAuthOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#passwordAuthOption.
    def exitPasswordAuthOption(self, ctx:SpeakQlParser.PasswordAuthOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#stringAuthOption.
    def enterStringAuthOption(self, ctx:SpeakQlParser.StringAuthOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#stringAuthOption.
    def exitStringAuthOption(self, ctx:SpeakQlParser.StringAuthOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#hashAuthOption.
    def enterHashAuthOption(self, ctx:SpeakQlParser.HashAuthOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#hashAuthOption.
    def exitHashAuthOption(self, ctx:SpeakQlParser.HashAuthOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#simpleAuthOption.
    def enterSimpleAuthOption(self, ctx:SpeakQlParser.SimpleAuthOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#simpleAuthOption.
    def exitSimpleAuthOption(self, ctx:SpeakQlParser.SimpleAuthOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tlsOption.
    def enterTlsOption(self, ctx:SpeakQlParser.TlsOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tlsOption.
    def exitTlsOption(self, ctx:SpeakQlParser.TlsOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#userResourceOption.
    def enterUserResourceOption(self, ctx:SpeakQlParser.UserResourceOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#userResourceOption.
    def exitUserResourceOption(self, ctx:SpeakQlParser.UserResourceOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#userPasswordOption.
    def enterUserPasswordOption(self, ctx:SpeakQlParser.UserPasswordOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#userPasswordOption.
    def exitUserPasswordOption(self, ctx:SpeakQlParser.UserPasswordOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#userLockOption.
    def enterUserLockOption(self, ctx:SpeakQlParser.UserLockOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#userLockOption.
    def exitUserLockOption(self, ctx:SpeakQlParser.UserLockOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#privelegeClause.
    def enterPrivelegeClause(self, ctx:SpeakQlParser.PrivelegeClauseContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#privelegeClause.
    def exitPrivelegeClause(self, ctx:SpeakQlParser.PrivelegeClauseContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#privilege.
    def enterPrivilege(self, ctx:SpeakQlParser.PrivilegeContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#privilege.
    def exitPrivilege(self, ctx:SpeakQlParser.PrivilegeContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#currentSchemaPriviLevel.
    def enterCurrentSchemaPriviLevel(self, ctx:SpeakQlParser.CurrentSchemaPriviLevelContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#currentSchemaPriviLevel.
    def exitCurrentSchemaPriviLevel(self, ctx:SpeakQlParser.CurrentSchemaPriviLevelContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#globalPrivLevel.
    def enterGlobalPrivLevel(self, ctx:SpeakQlParser.GlobalPrivLevelContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#globalPrivLevel.
    def exitGlobalPrivLevel(self, ctx:SpeakQlParser.GlobalPrivLevelContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#definiteSchemaPrivLevel.
    def enterDefiniteSchemaPrivLevel(self, ctx:SpeakQlParser.DefiniteSchemaPrivLevelContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#definiteSchemaPrivLevel.
    def exitDefiniteSchemaPrivLevel(self, ctx:SpeakQlParser.DefiniteSchemaPrivLevelContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#definiteFullTablePrivLevel.
    def enterDefiniteFullTablePrivLevel(self, ctx:SpeakQlParser.DefiniteFullTablePrivLevelContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#definiteFullTablePrivLevel.
    def exitDefiniteFullTablePrivLevel(self, ctx:SpeakQlParser.DefiniteFullTablePrivLevelContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#definiteFullTablePrivLevel2.
    def enterDefiniteFullTablePrivLevel2(self, ctx:SpeakQlParser.DefiniteFullTablePrivLevel2Context):
        pass

    # Exit a parse tree produced by SpeakQlParser#definiteFullTablePrivLevel2.
    def exitDefiniteFullTablePrivLevel2(self, ctx:SpeakQlParser.DefiniteFullTablePrivLevel2Context):
        pass


    # Enter a parse tree produced by SpeakQlParser#definiteTablePrivLevel.
    def enterDefiniteTablePrivLevel(self, ctx:SpeakQlParser.DefiniteTablePrivLevelContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#definiteTablePrivLevel.
    def exitDefiniteTablePrivLevel(self, ctx:SpeakQlParser.DefiniteTablePrivLevelContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#renameUserClause.
    def enterRenameUserClause(self, ctx:SpeakQlParser.RenameUserClauseContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#renameUserClause.
    def exitRenameUserClause(self, ctx:SpeakQlParser.RenameUserClauseContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#analyzeTable.
    def enterAnalyzeTable(self, ctx:SpeakQlParser.AnalyzeTableContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#analyzeTable.
    def exitAnalyzeTable(self, ctx:SpeakQlParser.AnalyzeTableContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#checkTable.
    def enterCheckTable(self, ctx:SpeakQlParser.CheckTableContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#checkTable.
    def exitCheckTable(self, ctx:SpeakQlParser.CheckTableContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#checksumTable.
    def enterChecksumTable(self, ctx:SpeakQlParser.ChecksumTableContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#checksumTable.
    def exitChecksumTable(self, ctx:SpeakQlParser.ChecksumTableContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#optimizeTable.
    def enterOptimizeTable(self, ctx:SpeakQlParser.OptimizeTableContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#optimizeTable.
    def exitOptimizeTable(self, ctx:SpeakQlParser.OptimizeTableContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#repairTable.
    def enterRepairTable(self, ctx:SpeakQlParser.RepairTableContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#repairTable.
    def exitRepairTable(self, ctx:SpeakQlParser.RepairTableContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#checkTableOption.
    def enterCheckTableOption(self, ctx:SpeakQlParser.CheckTableOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#checkTableOption.
    def exitCheckTableOption(self, ctx:SpeakQlParser.CheckTableOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#createUdfunction.
    def enterCreateUdfunction(self, ctx:SpeakQlParser.CreateUdfunctionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#createUdfunction.
    def exitCreateUdfunction(self, ctx:SpeakQlParser.CreateUdfunctionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#installPlugin.
    def enterInstallPlugin(self, ctx:SpeakQlParser.InstallPluginContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#installPlugin.
    def exitInstallPlugin(self, ctx:SpeakQlParser.InstallPluginContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#uninstallPlugin.
    def enterUninstallPlugin(self, ctx:SpeakQlParser.UninstallPluginContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#uninstallPlugin.
    def exitUninstallPlugin(self, ctx:SpeakQlParser.UninstallPluginContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#setVariable.
    def enterSetVariable(self, ctx:SpeakQlParser.SetVariableContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#setVariable.
    def exitSetVariable(self, ctx:SpeakQlParser.SetVariableContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#setCharset.
    def enterSetCharset(self, ctx:SpeakQlParser.SetCharsetContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#setCharset.
    def exitSetCharset(self, ctx:SpeakQlParser.SetCharsetContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#setNames.
    def enterSetNames(self, ctx:SpeakQlParser.SetNamesContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#setNames.
    def exitSetNames(self, ctx:SpeakQlParser.SetNamesContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#setPassword.
    def enterSetPassword(self, ctx:SpeakQlParser.SetPasswordContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#setPassword.
    def exitSetPassword(self, ctx:SpeakQlParser.SetPasswordContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#setTransaction.
    def enterSetTransaction(self, ctx:SpeakQlParser.SetTransactionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#setTransaction.
    def exitSetTransaction(self, ctx:SpeakQlParser.SetTransactionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#setAutocommit.
    def enterSetAutocommit(self, ctx:SpeakQlParser.SetAutocommitContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#setAutocommit.
    def exitSetAutocommit(self, ctx:SpeakQlParser.SetAutocommitContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#setNewValueInsideTrigger.
    def enterSetNewValueInsideTrigger(self, ctx:SpeakQlParser.SetNewValueInsideTriggerContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#setNewValueInsideTrigger.
    def exitSetNewValueInsideTrigger(self, ctx:SpeakQlParser.SetNewValueInsideTriggerContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#showMasterLogs.
    def enterShowMasterLogs(self, ctx:SpeakQlParser.ShowMasterLogsContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#showMasterLogs.
    def exitShowMasterLogs(self, ctx:SpeakQlParser.ShowMasterLogsContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#showLogEvents.
    def enterShowLogEvents(self, ctx:SpeakQlParser.ShowLogEventsContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#showLogEvents.
    def exitShowLogEvents(self, ctx:SpeakQlParser.ShowLogEventsContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#showObjectFilter.
    def enterShowObjectFilter(self, ctx:SpeakQlParser.ShowObjectFilterContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#showObjectFilter.
    def exitShowObjectFilter(self, ctx:SpeakQlParser.ShowObjectFilterContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#showColumns.
    def enterShowColumns(self, ctx:SpeakQlParser.ShowColumnsContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#showColumns.
    def exitShowColumns(self, ctx:SpeakQlParser.ShowColumnsContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#showCreateDb.
    def enterShowCreateDb(self, ctx:SpeakQlParser.ShowCreateDbContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#showCreateDb.
    def exitShowCreateDb(self, ctx:SpeakQlParser.ShowCreateDbContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#showCreateFullIdObject.
    def enterShowCreateFullIdObject(self, ctx:SpeakQlParser.ShowCreateFullIdObjectContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#showCreateFullIdObject.
    def exitShowCreateFullIdObject(self, ctx:SpeakQlParser.ShowCreateFullIdObjectContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#showCreateUser.
    def enterShowCreateUser(self, ctx:SpeakQlParser.ShowCreateUserContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#showCreateUser.
    def exitShowCreateUser(self, ctx:SpeakQlParser.ShowCreateUserContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#showEngine.
    def enterShowEngine(self, ctx:SpeakQlParser.ShowEngineContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#showEngine.
    def exitShowEngine(self, ctx:SpeakQlParser.ShowEngineContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#showGlobalInfo.
    def enterShowGlobalInfo(self, ctx:SpeakQlParser.ShowGlobalInfoContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#showGlobalInfo.
    def exitShowGlobalInfo(self, ctx:SpeakQlParser.ShowGlobalInfoContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#showErrors.
    def enterShowErrors(self, ctx:SpeakQlParser.ShowErrorsContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#showErrors.
    def exitShowErrors(self, ctx:SpeakQlParser.ShowErrorsContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#showCountErrors.
    def enterShowCountErrors(self, ctx:SpeakQlParser.ShowCountErrorsContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#showCountErrors.
    def exitShowCountErrors(self, ctx:SpeakQlParser.ShowCountErrorsContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#showSchemaFilter.
    def enterShowSchemaFilter(self, ctx:SpeakQlParser.ShowSchemaFilterContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#showSchemaFilter.
    def exitShowSchemaFilter(self, ctx:SpeakQlParser.ShowSchemaFilterContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#showRoutine.
    def enterShowRoutine(self, ctx:SpeakQlParser.ShowRoutineContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#showRoutine.
    def exitShowRoutine(self, ctx:SpeakQlParser.ShowRoutineContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#showGrants.
    def enterShowGrants(self, ctx:SpeakQlParser.ShowGrantsContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#showGrants.
    def exitShowGrants(self, ctx:SpeakQlParser.ShowGrantsContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#showIndexes.
    def enterShowIndexes(self, ctx:SpeakQlParser.ShowIndexesContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#showIndexes.
    def exitShowIndexes(self, ctx:SpeakQlParser.ShowIndexesContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#showOpenTables.
    def enterShowOpenTables(self, ctx:SpeakQlParser.ShowOpenTablesContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#showOpenTables.
    def exitShowOpenTables(self, ctx:SpeakQlParser.ShowOpenTablesContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#showProfile.
    def enterShowProfile(self, ctx:SpeakQlParser.ShowProfileContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#showProfile.
    def exitShowProfile(self, ctx:SpeakQlParser.ShowProfileContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#showSlaveStatus.
    def enterShowSlaveStatus(self, ctx:SpeakQlParser.ShowSlaveStatusContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#showSlaveStatus.
    def exitShowSlaveStatus(self, ctx:SpeakQlParser.ShowSlaveStatusContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#variableClause.
    def enterVariableClause(self, ctx:SpeakQlParser.VariableClauseContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#variableClause.
    def exitVariableClause(self, ctx:SpeakQlParser.VariableClauseContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#showCommonEntity.
    def enterShowCommonEntity(self, ctx:SpeakQlParser.ShowCommonEntityContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#showCommonEntity.
    def exitShowCommonEntity(self, ctx:SpeakQlParser.ShowCommonEntityContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#showFilter.
    def enterShowFilter(self, ctx:SpeakQlParser.ShowFilterContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#showFilter.
    def exitShowFilter(self, ctx:SpeakQlParser.ShowFilterContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#showGlobalInfoClause.
    def enterShowGlobalInfoClause(self, ctx:SpeakQlParser.ShowGlobalInfoClauseContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#showGlobalInfoClause.
    def exitShowGlobalInfoClause(self, ctx:SpeakQlParser.ShowGlobalInfoClauseContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#showSchemaEntity.
    def enterShowSchemaEntity(self, ctx:SpeakQlParser.ShowSchemaEntityContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#showSchemaEntity.
    def exitShowSchemaEntity(self, ctx:SpeakQlParser.ShowSchemaEntityContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#showProfileType.
    def enterShowProfileType(self, ctx:SpeakQlParser.ShowProfileTypeContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#showProfileType.
    def exitShowProfileType(self, ctx:SpeakQlParser.ShowProfileTypeContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#binlogStatement.
    def enterBinlogStatement(self, ctx:SpeakQlParser.BinlogStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#binlogStatement.
    def exitBinlogStatement(self, ctx:SpeakQlParser.BinlogStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#cacheIndexStatement.
    def enterCacheIndexStatement(self, ctx:SpeakQlParser.CacheIndexStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#cacheIndexStatement.
    def exitCacheIndexStatement(self, ctx:SpeakQlParser.CacheIndexStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#flushStatement.
    def enterFlushStatement(self, ctx:SpeakQlParser.FlushStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#flushStatement.
    def exitFlushStatement(self, ctx:SpeakQlParser.FlushStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#killStatement.
    def enterKillStatement(self, ctx:SpeakQlParser.KillStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#killStatement.
    def exitKillStatement(self, ctx:SpeakQlParser.KillStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#loadIndexIntoCache.
    def enterLoadIndexIntoCache(self, ctx:SpeakQlParser.LoadIndexIntoCacheContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#loadIndexIntoCache.
    def exitLoadIndexIntoCache(self, ctx:SpeakQlParser.LoadIndexIntoCacheContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#resetStatement.
    def enterResetStatement(self, ctx:SpeakQlParser.ResetStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#resetStatement.
    def exitResetStatement(self, ctx:SpeakQlParser.ResetStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#shutdownStatement.
    def enterShutdownStatement(self, ctx:SpeakQlParser.ShutdownStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#shutdownStatement.
    def exitShutdownStatement(self, ctx:SpeakQlParser.ShutdownStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableIndexes.
    def enterTableIndexes(self, ctx:SpeakQlParser.TableIndexesContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableIndexes.
    def exitTableIndexes(self, ctx:SpeakQlParser.TableIndexesContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#simpleFlushOption.
    def enterSimpleFlushOption(self, ctx:SpeakQlParser.SimpleFlushOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#simpleFlushOption.
    def exitSimpleFlushOption(self, ctx:SpeakQlParser.SimpleFlushOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#channelFlushOption.
    def enterChannelFlushOption(self, ctx:SpeakQlParser.ChannelFlushOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#channelFlushOption.
    def exitChannelFlushOption(self, ctx:SpeakQlParser.ChannelFlushOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableFlushOption.
    def enterTableFlushOption(self, ctx:SpeakQlParser.TableFlushOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableFlushOption.
    def exitTableFlushOption(self, ctx:SpeakQlParser.TableFlushOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#flushTableOption.
    def enterFlushTableOption(self, ctx:SpeakQlParser.FlushTableOptionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#flushTableOption.
    def exitFlushTableOption(self, ctx:SpeakQlParser.FlushTableOptionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#loadedTableIndexes.
    def enterLoadedTableIndexes(self, ctx:SpeakQlParser.LoadedTableIndexesContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#loadedTableIndexes.
    def exitLoadedTableIndexes(self, ctx:SpeakQlParser.LoadedTableIndexesContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#simpleDescribeStatement.
    def enterSimpleDescribeStatement(self, ctx:SpeakQlParser.SimpleDescribeStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#simpleDescribeStatement.
    def exitSimpleDescribeStatement(self, ctx:SpeakQlParser.SimpleDescribeStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#fullDescribeStatement.
    def enterFullDescribeStatement(self, ctx:SpeakQlParser.FullDescribeStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#fullDescribeStatement.
    def exitFullDescribeStatement(self, ctx:SpeakQlParser.FullDescribeStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#helpStatement.
    def enterHelpStatement(self, ctx:SpeakQlParser.HelpStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#helpStatement.
    def exitHelpStatement(self, ctx:SpeakQlParser.HelpStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#useStatement.
    def enterUseStatement(self, ctx:SpeakQlParser.UseStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#useStatement.
    def exitUseStatement(self, ctx:SpeakQlParser.UseStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#signalStatement.
    def enterSignalStatement(self, ctx:SpeakQlParser.SignalStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#signalStatement.
    def exitSignalStatement(self, ctx:SpeakQlParser.SignalStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#resignalStatement.
    def enterResignalStatement(self, ctx:SpeakQlParser.ResignalStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#resignalStatement.
    def exitResignalStatement(self, ctx:SpeakQlParser.ResignalStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#signalConditionInformation.
    def enterSignalConditionInformation(self, ctx:SpeakQlParser.SignalConditionInformationContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#signalConditionInformation.
    def exitSignalConditionInformation(self, ctx:SpeakQlParser.SignalConditionInformationContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#diagnosticsStatement.
    def enterDiagnosticsStatement(self, ctx:SpeakQlParser.DiagnosticsStatementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#diagnosticsStatement.
    def exitDiagnosticsStatement(self, ctx:SpeakQlParser.DiagnosticsStatementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#diagnosticsConditionInformationName.
    def enterDiagnosticsConditionInformationName(self, ctx:SpeakQlParser.DiagnosticsConditionInformationNameContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#diagnosticsConditionInformationName.
    def exitDiagnosticsConditionInformationName(self, ctx:SpeakQlParser.DiagnosticsConditionInformationNameContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#describeStatements.
    def enterDescribeStatements(self, ctx:SpeakQlParser.DescribeStatementsContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#describeStatements.
    def exitDescribeStatements(self, ctx:SpeakQlParser.DescribeStatementsContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#describeConnection.
    def enterDescribeConnection(self, ctx:SpeakQlParser.DescribeConnectionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#describeConnection.
    def exitDescribeConnection(self, ctx:SpeakQlParser.DescribeConnectionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#fullId.
    def enterFullId(self, ctx:SpeakQlParser.FullIdContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#fullId.
    def exitFullId(self, ctx:SpeakQlParser.FullIdContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tableName.
    def enterTableName(self, ctx:SpeakQlParser.TableNameContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tableName.
    def exitTableName(self, ctx:SpeakQlParser.TableNameContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#fullColumnName.
    def enterFullColumnName(self, ctx:SpeakQlParser.FullColumnNameContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#fullColumnName.
    def exitFullColumnName(self, ctx:SpeakQlParser.FullColumnNameContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#indexColumnName.
    def enterIndexColumnName(self, ctx:SpeakQlParser.IndexColumnNameContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#indexColumnName.
    def exitIndexColumnName(self, ctx:SpeakQlParser.IndexColumnNameContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#userName.
    def enterUserName(self, ctx:SpeakQlParser.UserNameContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#userName.
    def exitUserName(self, ctx:SpeakQlParser.UserNameContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#mysqlVariable.
    def enterMysqlVariable(self, ctx:SpeakQlParser.MysqlVariableContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#mysqlVariable.
    def exitMysqlVariable(self, ctx:SpeakQlParser.MysqlVariableContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#charsetName.
    def enterCharsetName(self, ctx:SpeakQlParser.CharsetNameContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#charsetName.
    def exitCharsetName(self, ctx:SpeakQlParser.CharsetNameContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#collationName.
    def enterCollationName(self, ctx:SpeakQlParser.CollationNameContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#collationName.
    def exitCollationName(self, ctx:SpeakQlParser.CollationNameContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#engineName.
    def enterEngineName(self, ctx:SpeakQlParser.EngineNameContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#engineName.
    def exitEngineName(self, ctx:SpeakQlParser.EngineNameContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#uuidSet.
    def enterUuidSet(self, ctx:SpeakQlParser.UuidSetContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#uuidSet.
    def exitUuidSet(self, ctx:SpeakQlParser.UuidSetContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#xid.
    def enterXid(self, ctx:SpeakQlParser.XidContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#xid.
    def exitXid(self, ctx:SpeakQlParser.XidContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#xuidStringId.
    def enterXuidStringId(self, ctx:SpeakQlParser.XuidStringIdContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#xuidStringId.
    def exitXuidStringId(self, ctx:SpeakQlParser.XuidStringIdContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#authPlugin.
    def enterAuthPlugin(self, ctx:SpeakQlParser.AuthPluginContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#authPlugin.
    def exitAuthPlugin(self, ctx:SpeakQlParser.AuthPluginContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#uid.
    def enterUid(self, ctx:SpeakQlParser.UidContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#uid.
    def exitUid(self, ctx:SpeakQlParser.UidContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#simpleId.
    def enterSimpleId(self, ctx:SpeakQlParser.SimpleIdContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#simpleId.
    def exitSimpleId(self, ctx:SpeakQlParser.SimpleIdContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#dottedId.
    def enterDottedId(self, ctx:SpeakQlParser.DottedIdContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#dottedId.
    def exitDottedId(self, ctx:SpeakQlParser.DottedIdContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#decimalLiteral.
    def enterDecimalLiteral(self, ctx:SpeakQlParser.DecimalLiteralContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#decimalLiteral.
    def exitDecimalLiteral(self, ctx:SpeakQlParser.DecimalLiteralContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#fileSizeLiteral.
    def enterFileSizeLiteral(self, ctx:SpeakQlParser.FileSizeLiteralContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#fileSizeLiteral.
    def exitFileSizeLiteral(self, ctx:SpeakQlParser.FileSizeLiteralContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#stringLiteral.
    def enterStringLiteral(self, ctx:SpeakQlParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#stringLiteral.
    def exitStringLiteral(self, ctx:SpeakQlParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:SpeakQlParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:SpeakQlParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#hexadecimalLiteral.
    def enterHexadecimalLiteral(self, ctx:SpeakQlParser.HexadecimalLiteralContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#hexadecimalLiteral.
    def exitHexadecimalLiteral(self, ctx:SpeakQlParser.HexadecimalLiteralContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#nullNotnull.
    def enterNullNotnull(self, ctx:SpeakQlParser.NullNotnullContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#nullNotnull.
    def exitNullNotnull(self, ctx:SpeakQlParser.NullNotnullContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#constant.
    def enterConstant(self, ctx:SpeakQlParser.ConstantContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#constant.
    def exitConstant(self, ctx:SpeakQlParser.ConstantContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#stringDataType.
    def enterStringDataType(self, ctx:SpeakQlParser.StringDataTypeContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#stringDataType.
    def exitStringDataType(self, ctx:SpeakQlParser.StringDataTypeContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#nationalStringDataType.
    def enterNationalStringDataType(self, ctx:SpeakQlParser.NationalStringDataTypeContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#nationalStringDataType.
    def exitNationalStringDataType(self, ctx:SpeakQlParser.NationalStringDataTypeContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#nationalVaryingStringDataType.
    def enterNationalVaryingStringDataType(self, ctx:SpeakQlParser.NationalVaryingStringDataTypeContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#nationalVaryingStringDataType.
    def exitNationalVaryingStringDataType(self, ctx:SpeakQlParser.NationalVaryingStringDataTypeContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#dimensionDataType.
    def enterDimensionDataType(self, ctx:SpeakQlParser.DimensionDataTypeContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#dimensionDataType.
    def exitDimensionDataType(self, ctx:SpeakQlParser.DimensionDataTypeContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#simpleDataType.
    def enterSimpleDataType(self, ctx:SpeakQlParser.SimpleDataTypeContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#simpleDataType.
    def exitSimpleDataType(self, ctx:SpeakQlParser.SimpleDataTypeContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#collectionDataType.
    def enterCollectionDataType(self, ctx:SpeakQlParser.CollectionDataTypeContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#collectionDataType.
    def exitCollectionDataType(self, ctx:SpeakQlParser.CollectionDataTypeContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#spatialDataType.
    def enterSpatialDataType(self, ctx:SpeakQlParser.SpatialDataTypeContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#spatialDataType.
    def exitSpatialDataType(self, ctx:SpeakQlParser.SpatialDataTypeContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#longVarcharDataType.
    def enterLongVarcharDataType(self, ctx:SpeakQlParser.LongVarcharDataTypeContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#longVarcharDataType.
    def exitLongVarcharDataType(self, ctx:SpeakQlParser.LongVarcharDataTypeContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#longVarbinaryDataType.
    def enterLongVarbinaryDataType(self, ctx:SpeakQlParser.LongVarbinaryDataTypeContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#longVarbinaryDataType.
    def exitLongVarbinaryDataType(self, ctx:SpeakQlParser.LongVarbinaryDataTypeContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#collectionOptions.
    def enterCollectionOptions(self, ctx:SpeakQlParser.CollectionOptionsContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#collectionOptions.
    def exitCollectionOptions(self, ctx:SpeakQlParser.CollectionOptionsContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#convertedDataType.
    def enterConvertedDataType(self, ctx:SpeakQlParser.ConvertedDataTypeContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#convertedDataType.
    def exitConvertedDataType(self, ctx:SpeakQlParser.ConvertedDataTypeContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#lengthOneDimension.
    def enterLengthOneDimension(self, ctx:SpeakQlParser.LengthOneDimensionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#lengthOneDimension.
    def exitLengthOneDimension(self, ctx:SpeakQlParser.LengthOneDimensionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#lengthTwoDimension.
    def enterLengthTwoDimension(self, ctx:SpeakQlParser.LengthTwoDimensionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#lengthTwoDimension.
    def exitLengthTwoDimension(self, ctx:SpeakQlParser.LengthTwoDimensionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#lengthTwoOptionalDimension.
    def enterLengthTwoOptionalDimension(self, ctx:SpeakQlParser.LengthTwoOptionalDimensionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#lengthTwoOptionalDimension.
    def exitLengthTwoOptionalDimension(self, ctx:SpeakQlParser.LengthTwoOptionalDimensionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#uidList.
    def enterUidList(self, ctx:SpeakQlParser.UidListContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#uidList.
    def exitUidList(self, ctx:SpeakQlParser.UidListContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#tables.
    def enterTables(self, ctx:SpeakQlParser.TablesContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#tables.
    def exitTables(self, ctx:SpeakQlParser.TablesContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#indexColumnNames.
    def enterIndexColumnNames(self, ctx:SpeakQlParser.IndexColumnNamesContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#indexColumnNames.
    def exitIndexColumnNames(self, ctx:SpeakQlParser.IndexColumnNamesContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#expressions.
    def enterExpressions(self, ctx:SpeakQlParser.ExpressionsContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#expressions.
    def exitExpressions(self, ctx:SpeakQlParser.ExpressionsContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#expressionsWithDefaults.
    def enterExpressionsWithDefaults(self, ctx:SpeakQlParser.ExpressionsWithDefaultsContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#expressionsWithDefaults.
    def exitExpressionsWithDefaults(self, ctx:SpeakQlParser.ExpressionsWithDefaultsContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#constants.
    def enterConstants(self, ctx:SpeakQlParser.ConstantsContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#constants.
    def exitConstants(self, ctx:SpeakQlParser.ConstantsContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#simpleStrings.
    def enterSimpleStrings(self, ctx:SpeakQlParser.SimpleStringsContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#simpleStrings.
    def exitSimpleStrings(self, ctx:SpeakQlParser.SimpleStringsContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#userVariables.
    def enterUserVariables(self, ctx:SpeakQlParser.UserVariablesContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#userVariables.
    def exitUserVariables(self, ctx:SpeakQlParser.UserVariablesContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#defaultValue.
    def enterDefaultValue(self, ctx:SpeakQlParser.DefaultValueContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#defaultValue.
    def exitDefaultValue(self, ctx:SpeakQlParser.DefaultValueContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#currentTimestamp.
    def enterCurrentTimestamp(self, ctx:SpeakQlParser.CurrentTimestampContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#currentTimestamp.
    def exitCurrentTimestamp(self, ctx:SpeakQlParser.CurrentTimestampContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#expressionOrDefault.
    def enterExpressionOrDefault(self, ctx:SpeakQlParser.ExpressionOrDefaultContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#expressionOrDefault.
    def exitExpressionOrDefault(self, ctx:SpeakQlParser.ExpressionOrDefaultContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#ifExists.
    def enterIfExists(self, ctx:SpeakQlParser.IfExistsContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#ifExists.
    def exitIfExists(self, ctx:SpeakQlParser.IfExistsContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#ifNotExists.
    def enterIfNotExists(self, ctx:SpeakQlParser.IfNotExistsContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#ifNotExists.
    def exitIfNotExists(self, ctx:SpeakQlParser.IfNotExistsContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#specificFunctionCall.
    def enterSpecificFunctionCall(self, ctx:SpeakQlParser.SpecificFunctionCallContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#specificFunctionCall.
    def exitSpecificFunctionCall(self, ctx:SpeakQlParser.SpecificFunctionCallContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#aggregateFunctionCall.
    def enterAggregateFunctionCall(self, ctx:SpeakQlParser.AggregateFunctionCallContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#aggregateFunctionCall.
    def exitAggregateFunctionCall(self, ctx:SpeakQlParser.AggregateFunctionCallContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#nonAggregateFunctionCall.
    def enterNonAggregateFunctionCall(self, ctx:SpeakQlParser.NonAggregateFunctionCallContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#nonAggregateFunctionCall.
    def exitNonAggregateFunctionCall(self, ctx:SpeakQlParser.NonAggregateFunctionCallContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#scalarFunctionCall.
    def enterScalarFunctionCall(self, ctx:SpeakQlParser.ScalarFunctionCallContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#scalarFunctionCall.
    def exitScalarFunctionCall(self, ctx:SpeakQlParser.ScalarFunctionCallContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#udfFunctionCall.
    def enterUdfFunctionCall(self, ctx:SpeakQlParser.UdfFunctionCallContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#udfFunctionCall.
    def exitUdfFunctionCall(self, ctx:SpeakQlParser.UdfFunctionCallContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#passwordFunctionCall.
    def enterPasswordFunctionCall(self, ctx:SpeakQlParser.PasswordFunctionCallContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#passwordFunctionCall.
    def exitPasswordFunctionCall(self, ctx:SpeakQlParser.PasswordFunctionCallContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#leftParen.
    def enterLeftParen(self, ctx:SpeakQlParser.LeftParenContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#leftParen.
    def exitLeftParen(self, ctx:SpeakQlParser.LeftParenContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#rightParen.
    def enterRightParen(self, ctx:SpeakQlParser.RightParenContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#rightParen.
    def exitRightParen(self, ctx:SpeakQlParser.RightParenContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#simpleFunctionCall.
    def enterSimpleFunctionCall(self, ctx:SpeakQlParser.SimpleFunctionCallContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#simpleFunctionCall.
    def exitSimpleFunctionCall(self, ctx:SpeakQlParser.SimpleFunctionCallContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#dataTypeFunctionCall.
    def enterDataTypeFunctionCall(self, ctx:SpeakQlParser.DataTypeFunctionCallContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#dataTypeFunctionCall.
    def exitDataTypeFunctionCall(self, ctx:SpeakQlParser.DataTypeFunctionCallContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#valuesFunctionCall.
    def enterValuesFunctionCall(self, ctx:SpeakQlParser.ValuesFunctionCallContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#valuesFunctionCall.
    def exitValuesFunctionCall(self, ctx:SpeakQlParser.ValuesFunctionCallContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#caseExpressionFunctionCall.
    def enterCaseExpressionFunctionCall(self, ctx:SpeakQlParser.CaseExpressionFunctionCallContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#caseExpressionFunctionCall.
    def exitCaseExpressionFunctionCall(self, ctx:SpeakQlParser.CaseExpressionFunctionCallContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#caseFunctionCall.
    def enterCaseFunctionCall(self, ctx:SpeakQlParser.CaseFunctionCallContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#caseFunctionCall.
    def exitCaseFunctionCall(self, ctx:SpeakQlParser.CaseFunctionCallContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#charFunctionCall.
    def enterCharFunctionCall(self, ctx:SpeakQlParser.CharFunctionCallContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#charFunctionCall.
    def exitCharFunctionCall(self, ctx:SpeakQlParser.CharFunctionCallContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#positionFunctionCall.
    def enterPositionFunctionCall(self, ctx:SpeakQlParser.PositionFunctionCallContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#positionFunctionCall.
    def exitPositionFunctionCall(self, ctx:SpeakQlParser.PositionFunctionCallContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#substrFunctionCall.
    def enterSubstrFunctionCall(self, ctx:SpeakQlParser.SubstrFunctionCallContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#substrFunctionCall.
    def exitSubstrFunctionCall(self, ctx:SpeakQlParser.SubstrFunctionCallContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#trimFunctionCall.
    def enterTrimFunctionCall(self, ctx:SpeakQlParser.TrimFunctionCallContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#trimFunctionCall.
    def exitTrimFunctionCall(self, ctx:SpeakQlParser.TrimFunctionCallContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#weightFunctionCall.
    def enterWeightFunctionCall(self, ctx:SpeakQlParser.WeightFunctionCallContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#weightFunctionCall.
    def exitWeightFunctionCall(self, ctx:SpeakQlParser.WeightFunctionCallContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#extractFunctionCall.
    def enterExtractFunctionCall(self, ctx:SpeakQlParser.ExtractFunctionCallContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#extractFunctionCall.
    def exitExtractFunctionCall(self, ctx:SpeakQlParser.ExtractFunctionCallContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#getFormatFunctionCall.
    def enterGetFormatFunctionCall(self, ctx:SpeakQlParser.GetFormatFunctionCallContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#getFormatFunctionCall.
    def exitGetFormatFunctionCall(self, ctx:SpeakQlParser.GetFormatFunctionCallContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#jsonValueFunctionCall.
    def enterJsonValueFunctionCall(self, ctx:SpeakQlParser.JsonValueFunctionCallContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#jsonValueFunctionCall.
    def exitJsonValueFunctionCall(self, ctx:SpeakQlParser.JsonValueFunctionCallContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#caseFuncAlternative.
    def enterCaseFuncAlternative(self, ctx:SpeakQlParser.CaseFuncAlternativeContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#caseFuncAlternative.
    def exitCaseFuncAlternative(self, ctx:SpeakQlParser.CaseFuncAlternativeContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#levelWeightList.
    def enterLevelWeightList(self, ctx:SpeakQlParser.LevelWeightListContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#levelWeightList.
    def exitLevelWeightList(self, ctx:SpeakQlParser.LevelWeightListContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#levelWeightRange.
    def enterLevelWeightRange(self, ctx:SpeakQlParser.LevelWeightRangeContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#levelWeightRange.
    def exitLevelWeightRange(self, ctx:SpeakQlParser.LevelWeightRangeContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#levelInWeightListElement.
    def enterLevelInWeightListElement(self, ctx:SpeakQlParser.LevelInWeightListElementContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#levelInWeightListElement.
    def exitLevelInWeightListElement(self, ctx:SpeakQlParser.LevelInWeightListElementContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#aggregateWindowedFunction.
    def enterAggregateWindowedFunction(self, ctx:SpeakQlParser.AggregateWindowedFunctionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#aggregateWindowedFunction.
    def exitAggregateWindowedFunction(self, ctx:SpeakQlParser.AggregateWindowedFunctionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#nonAggregateWindowedFunction.
    def enterNonAggregateWindowedFunction(self, ctx:SpeakQlParser.NonAggregateWindowedFunctionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#nonAggregateWindowedFunction.
    def exitNonAggregateWindowedFunction(self, ctx:SpeakQlParser.NonAggregateWindowedFunctionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#overClause.
    def enterOverClause(self, ctx:SpeakQlParser.OverClauseContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#overClause.
    def exitOverClause(self, ctx:SpeakQlParser.OverClauseContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#windowSpec.
    def enterWindowSpec(self, ctx:SpeakQlParser.WindowSpecContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#windowSpec.
    def exitWindowSpec(self, ctx:SpeakQlParser.WindowSpecContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#windowName.
    def enterWindowName(self, ctx:SpeakQlParser.WindowNameContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#windowName.
    def exitWindowName(self, ctx:SpeakQlParser.WindowNameContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#frameClause.
    def enterFrameClause(self, ctx:SpeakQlParser.FrameClauseContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#frameClause.
    def exitFrameClause(self, ctx:SpeakQlParser.FrameClauseContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#frameUnits.
    def enterFrameUnits(self, ctx:SpeakQlParser.FrameUnitsContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#frameUnits.
    def exitFrameUnits(self, ctx:SpeakQlParser.FrameUnitsContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#frameExtent.
    def enterFrameExtent(self, ctx:SpeakQlParser.FrameExtentContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#frameExtent.
    def exitFrameExtent(self, ctx:SpeakQlParser.FrameExtentContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#frameBetween.
    def enterFrameBetween(self, ctx:SpeakQlParser.FrameBetweenContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#frameBetween.
    def exitFrameBetween(self, ctx:SpeakQlParser.FrameBetweenContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#frameRange.
    def enterFrameRange(self, ctx:SpeakQlParser.FrameRangeContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#frameRange.
    def exitFrameRange(self, ctx:SpeakQlParser.FrameRangeContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#partitionClause.
    def enterPartitionClause(self, ctx:SpeakQlParser.PartitionClauseContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#partitionClause.
    def exitPartitionClause(self, ctx:SpeakQlParser.PartitionClauseContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#scalarFunctionName.
    def enterScalarFunctionName(self, ctx:SpeakQlParser.ScalarFunctionNameContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#scalarFunctionName.
    def exitScalarFunctionName(self, ctx:SpeakQlParser.ScalarFunctionNameContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#passwordFunctionClause.
    def enterPasswordFunctionClause(self, ctx:SpeakQlParser.PasswordFunctionClauseContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#passwordFunctionClause.
    def exitPasswordFunctionClause(self, ctx:SpeakQlParser.PasswordFunctionClauseContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#functionArgs.
    def enterFunctionArgs(self, ctx:SpeakQlParser.FunctionArgsContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#functionArgs.
    def exitFunctionArgs(self, ctx:SpeakQlParser.FunctionArgsContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#functionArg.
    def enterFunctionArg(self, ctx:SpeakQlParser.FunctionArgContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#functionArg.
    def exitFunctionArg(self, ctx:SpeakQlParser.FunctionArgContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#isExpression.
    def enterIsExpression(self, ctx:SpeakQlParser.IsExpressionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#isExpression.
    def exitIsExpression(self, ctx:SpeakQlParser.IsExpressionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#notExpression.
    def enterNotExpression(self, ctx:SpeakQlParser.NotExpressionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#notExpression.
    def exitNotExpression(self, ctx:SpeakQlParser.NotExpressionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#logicalExpression.
    def enterLogicalExpression(self, ctx:SpeakQlParser.LogicalExpressionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#logicalExpression.
    def exitLogicalExpression(self, ctx:SpeakQlParser.LogicalExpressionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#predicateExpression.
    def enterPredicateExpression(self, ctx:SpeakQlParser.PredicateExpressionContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#predicateExpression.
    def exitPredicateExpression(self, ctx:SpeakQlParser.PredicateExpressionContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#soundsLikePredicate.
    def enterSoundsLikePredicate(self, ctx:SpeakQlParser.SoundsLikePredicateContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#soundsLikePredicate.
    def exitSoundsLikePredicate(self, ctx:SpeakQlParser.SoundsLikePredicateContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#expressionAtomPredicate.
    def enterExpressionAtomPredicate(self, ctx:SpeakQlParser.ExpressionAtomPredicateContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#expressionAtomPredicate.
    def exitExpressionAtomPredicate(self, ctx:SpeakQlParser.ExpressionAtomPredicateContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#subqueryComparisonPredicate.
    def enterSubqueryComparisonPredicate(self, ctx:SpeakQlParser.SubqueryComparisonPredicateContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#subqueryComparisonPredicate.
    def exitSubqueryComparisonPredicate(self, ctx:SpeakQlParser.SubqueryComparisonPredicateContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#jsonMemberOfPredicate.
    def enterJsonMemberOfPredicate(self, ctx:SpeakQlParser.JsonMemberOfPredicateContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#jsonMemberOfPredicate.
    def exitJsonMemberOfPredicate(self, ctx:SpeakQlParser.JsonMemberOfPredicateContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#binaryComparisonPredicate.
    def enterBinaryComparisonPredicate(self, ctx:SpeakQlParser.BinaryComparisonPredicateContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#binaryComparisonPredicate.
    def exitBinaryComparisonPredicate(self, ctx:SpeakQlParser.BinaryComparisonPredicateContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#inPredicate.
    def enterInPredicate(self, ctx:SpeakQlParser.InPredicateContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#inPredicate.
    def exitInPredicate(self, ctx:SpeakQlParser.InPredicateContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#betweenPredicate.
    def enterBetweenPredicate(self, ctx:SpeakQlParser.BetweenPredicateContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#betweenPredicate.
    def exitBetweenPredicate(self, ctx:SpeakQlParser.BetweenPredicateContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#isNullPredicate.
    def enterIsNullPredicate(self, ctx:SpeakQlParser.IsNullPredicateContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#isNullPredicate.
    def exitIsNullPredicate(self, ctx:SpeakQlParser.IsNullPredicateContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#likePredicate.
    def enterLikePredicate(self, ctx:SpeakQlParser.LikePredicateContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#likePredicate.
    def exitLikePredicate(self, ctx:SpeakQlParser.LikePredicateContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#regexpPredicate.
    def enterRegexpPredicate(self, ctx:SpeakQlParser.RegexpPredicateContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#regexpPredicate.
    def exitRegexpPredicate(self, ctx:SpeakQlParser.RegexpPredicateContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#unaryExpressionAtom.
    def enterUnaryExpressionAtom(self, ctx:SpeakQlParser.UnaryExpressionAtomContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#unaryExpressionAtom.
    def exitUnaryExpressionAtom(self, ctx:SpeakQlParser.UnaryExpressionAtomContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#collateExpressionAtom.
    def enterCollateExpressionAtom(self, ctx:SpeakQlParser.CollateExpressionAtomContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#collateExpressionAtom.
    def exitCollateExpressionAtom(self, ctx:SpeakQlParser.CollateExpressionAtomContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#mysqlVariableExpressionAtom.
    def enterMysqlVariableExpressionAtom(self, ctx:SpeakQlParser.MysqlVariableExpressionAtomContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#mysqlVariableExpressionAtom.
    def exitMysqlVariableExpressionAtom(self, ctx:SpeakQlParser.MysqlVariableExpressionAtomContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#nestedExpressionAtom.
    def enterNestedExpressionAtom(self, ctx:SpeakQlParser.NestedExpressionAtomContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#nestedExpressionAtom.
    def exitNestedExpressionAtom(self, ctx:SpeakQlParser.NestedExpressionAtomContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#nestedRowExpressionAtom.
    def enterNestedRowExpressionAtom(self, ctx:SpeakQlParser.NestedRowExpressionAtomContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#nestedRowExpressionAtom.
    def exitNestedRowExpressionAtom(self, ctx:SpeakQlParser.NestedRowExpressionAtomContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#mathExpressionAtom.
    def enterMathExpressionAtom(self, ctx:SpeakQlParser.MathExpressionAtomContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#mathExpressionAtom.
    def exitMathExpressionAtom(self, ctx:SpeakQlParser.MathExpressionAtomContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#existsExpressionAtom.
    def enterExistsExpressionAtom(self, ctx:SpeakQlParser.ExistsExpressionAtomContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#existsExpressionAtom.
    def exitExistsExpressionAtom(self, ctx:SpeakQlParser.ExistsExpressionAtomContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#intervalExpressionAtom.
    def enterIntervalExpressionAtom(self, ctx:SpeakQlParser.IntervalExpressionAtomContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#intervalExpressionAtom.
    def exitIntervalExpressionAtom(self, ctx:SpeakQlParser.IntervalExpressionAtomContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#jsonExpressionAtom.
    def enterJsonExpressionAtom(self, ctx:SpeakQlParser.JsonExpressionAtomContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#jsonExpressionAtom.
    def exitJsonExpressionAtom(self, ctx:SpeakQlParser.JsonExpressionAtomContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#subqueryExpressionAtom.
    def enterSubqueryExpressionAtom(self, ctx:SpeakQlParser.SubqueryExpressionAtomContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#subqueryExpressionAtom.
    def exitSubqueryExpressionAtom(self, ctx:SpeakQlParser.SubqueryExpressionAtomContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#constantExpressionAtom.
    def enterConstantExpressionAtom(self, ctx:SpeakQlParser.ConstantExpressionAtomContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#constantExpressionAtom.
    def exitConstantExpressionAtom(self, ctx:SpeakQlParser.ConstantExpressionAtomContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#functionCallExpressionAtom.
    def enterFunctionCallExpressionAtom(self, ctx:SpeakQlParser.FunctionCallExpressionAtomContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#functionCallExpressionAtom.
    def exitFunctionCallExpressionAtom(self, ctx:SpeakQlParser.FunctionCallExpressionAtomContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#binaryExpressionAtom.
    def enterBinaryExpressionAtom(self, ctx:SpeakQlParser.BinaryExpressionAtomContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#binaryExpressionAtom.
    def exitBinaryExpressionAtom(self, ctx:SpeakQlParser.BinaryExpressionAtomContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#fullColumnNameExpressionAtom.
    def enterFullColumnNameExpressionAtom(self, ctx:SpeakQlParser.FullColumnNameExpressionAtomContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#fullColumnNameExpressionAtom.
    def exitFullColumnNameExpressionAtom(self, ctx:SpeakQlParser.FullColumnNameExpressionAtomContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#bitExpressionAtom.
    def enterBitExpressionAtom(self, ctx:SpeakQlParser.BitExpressionAtomContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#bitExpressionAtom.
    def exitBitExpressionAtom(self, ctx:SpeakQlParser.BitExpressionAtomContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#unaryOperator.
    def enterUnaryOperator(self, ctx:SpeakQlParser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#unaryOperator.
    def exitUnaryOperator(self, ctx:SpeakQlParser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:SpeakQlParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:SpeakQlParser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#logicalOperator.
    def enterLogicalOperator(self, ctx:SpeakQlParser.LogicalOperatorContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#logicalOperator.
    def exitLogicalOperator(self, ctx:SpeakQlParser.LogicalOperatorContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#bitOperator.
    def enterBitOperator(self, ctx:SpeakQlParser.BitOperatorContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#bitOperator.
    def exitBitOperator(self, ctx:SpeakQlParser.BitOperatorContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#mathOperator.
    def enterMathOperator(self, ctx:SpeakQlParser.MathOperatorContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#mathOperator.
    def exitMathOperator(self, ctx:SpeakQlParser.MathOperatorContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#jsonOperator.
    def enterJsonOperator(self, ctx:SpeakQlParser.JsonOperatorContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#jsonOperator.
    def exitJsonOperator(self, ctx:SpeakQlParser.JsonOperatorContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#charsetNameBase.
    def enterCharsetNameBase(self, ctx:SpeakQlParser.CharsetNameBaseContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#charsetNameBase.
    def exitCharsetNameBase(self, ctx:SpeakQlParser.CharsetNameBaseContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#transactionLevelBase.
    def enterTransactionLevelBase(self, ctx:SpeakQlParser.TransactionLevelBaseContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#transactionLevelBase.
    def exitTransactionLevelBase(self, ctx:SpeakQlParser.TransactionLevelBaseContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#privilegesBase.
    def enterPrivilegesBase(self, ctx:SpeakQlParser.PrivilegesBaseContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#privilegesBase.
    def exitPrivilegesBase(self, ctx:SpeakQlParser.PrivilegesBaseContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#intervalTypeBase.
    def enterIntervalTypeBase(self, ctx:SpeakQlParser.IntervalTypeBaseContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#intervalTypeBase.
    def exitIntervalTypeBase(self, ctx:SpeakQlParser.IntervalTypeBaseContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#dataTypeBase.
    def enterDataTypeBase(self, ctx:SpeakQlParser.DataTypeBaseContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#dataTypeBase.
    def exitDataTypeBase(self, ctx:SpeakQlParser.DataTypeBaseContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#keywordsCanBeId.
    def enterKeywordsCanBeId(self, ctx:SpeakQlParser.KeywordsCanBeIdContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#keywordsCanBeId.
    def exitKeywordsCanBeId(self, ctx:SpeakQlParser.KeywordsCanBeIdContext):
        pass


    # Enter a parse tree produced by SpeakQlParser#functionNameBase.
    def enterFunctionNameBase(self, ctx:SpeakQlParser.FunctionNameBaseContext):
        pass

    # Exit a parse tree produced by SpeakQlParser#functionNameBase.
    def exitFunctionNameBase(self, ctx:SpeakQlParser.FunctionNameBaseContext):
        pass



del SpeakQlParser
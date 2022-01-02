# Generated from SpeakQlParser.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SpeakQlParser import SpeakQlParser
else:
    from SpeakQlParser import SpeakQlParser

# This class defines a complete generic visitor for a parse tree produced by SpeakQlParser.

class SpeakQlParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SpeakQlParser#root.
    def visitRoot(self, ctx:SpeakQlParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#sqlStatements.
    def visitSqlStatements(self, ctx:SpeakQlParser.SqlStatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#sqlStatement.
    def visitSqlStatement(self, ctx:SpeakQlParser.SqlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#emptyStatement.
    def visitEmptyStatement(self, ctx:SpeakQlParser.EmptyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#ddlStatement.
    def visitDdlStatement(self, ctx:SpeakQlParser.DdlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#dmlStatement.
    def visitDmlStatement(self, ctx:SpeakQlParser.DmlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#transactionStatement.
    def visitTransactionStatement(self, ctx:SpeakQlParser.TransactionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#replicationStatement.
    def visitReplicationStatement(self, ctx:SpeakQlParser.ReplicationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#preparedStatement.
    def visitPreparedStatement(self, ctx:SpeakQlParser.PreparedStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#compoundStatement.
    def visitCompoundStatement(self, ctx:SpeakQlParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#administrationStatement.
    def visitAdministrationStatement(self, ctx:SpeakQlParser.AdministrationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#utilityStatement.
    def visitUtilityStatement(self, ctx:SpeakQlParser.UtilityStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#createDatabase.
    def visitCreateDatabase(self, ctx:SpeakQlParser.CreateDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#createEvent.
    def visitCreateEvent(self, ctx:SpeakQlParser.CreateEventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#createIndex.
    def visitCreateIndex(self, ctx:SpeakQlParser.CreateIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#createLogfileGroup.
    def visitCreateLogfileGroup(self, ctx:SpeakQlParser.CreateLogfileGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#createProcedure.
    def visitCreateProcedure(self, ctx:SpeakQlParser.CreateProcedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#createFunction.
    def visitCreateFunction(self, ctx:SpeakQlParser.CreateFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#createServer.
    def visitCreateServer(self, ctx:SpeakQlParser.CreateServerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#copyCreateTable.
    def visitCopyCreateTable(self, ctx:SpeakQlParser.CopyCreateTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#queryCreateTable.
    def visitQueryCreateTable(self, ctx:SpeakQlParser.QueryCreateTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#columnCreateTable.
    def visitColumnCreateTable(self, ctx:SpeakQlParser.ColumnCreateTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#createTablespaceInnodb.
    def visitCreateTablespaceInnodb(self, ctx:SpeakQlParser.CreateTablespaceInnodbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#createTablespaceNdb.
    def visitCreateTablespaceNdb(self, ctx:SpeakQlParser.CreateTablespaceNdbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#createTrigger.
    def visitCreateTrigger(self, ctx:SpeakQlParser.CreateTriggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#createView.
    def visitCreateView(self, ctx:SpeakQlParser.CreateViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#createDatabaseOption.
    def visitCreateDatabaseOption(self, ctx:SpeakQlParser.CreateDatabaseOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#ownerStatement.
    def visitOwnerStatement(self, ctx:SpeakQlParser.OwnerStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#preciseSchedule.
    def visitPreciseSchedule(self, ctx:SpeakQlParser.PreciseScheduleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#intervalSchedule.
    def visitIntervalSchedule(self, ctx:SpeakQlParser.IntervalScheduleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#timestampValue.
    def visitTimestampValue(self, ctx:SpeakQlParser.TimestampValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#intervalExpr.
    def visitIntervalExpr(self, ctx:SpeakQlParser.IntervalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#intervalType.
    def visitIntervalType(self, ctx:SpeakQlParser.IntervalTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#enableType.
    def visitEnableType(self, ctx:SpeakQlParser.EnableTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#indexType.
    def visitIndexType(self, ctx:SpeakQlParser.IndexTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#indexOption.
    def visitIndexOption(self, ctx:SpeakQlParser.IndexOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#procedureParameter.
    def visitProcedureParameter(self, ctx:SpeakQlParser.ProcedureParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#functionParameter.
    def visitFunctionParameter(self, ctx:SpeakQlParser.FunctionParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#routineComment.
    def visitRoutineComment(self, ctx:SpeakQlParser.RoutineCommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#routineLanguage.
    def visitRoutineLanguage(self, ctx:SpeakQlParser.RoutineLanguageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#routineBehavior.
    def visitRoutineBehavior(self, ctx:SpeakQlParser.RoutineBehaviorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#routineData.
    def visitRoutineData(self, ctx:SpeakQlParser.RoutineDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#routineSecurity.
    def visitRoutineSecurity(self, ctx:SpeakQlParser.RoutineSecurityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#serverOption.
    def visitServerOption(self, ctx:SpeakQlParser.ServerOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#createDefinitions.
    def visitCreateDefinitions(self, ctx:SpeakQlParser.CreateDefinitionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#columnDeclaration.
    def visitColumnDeclaration(self, ctx:SpeakQlParser.ColumnDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#constraintDeclaration.
    def visitConstraintDeclaration(self, ctx:SpeakQlParser.ConstraintDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#indexDeclaration.
    def visitIndexDeclaration(self, ctx:SpeakQlParser.IndexDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#columnDefinition.
    def visitColumnDefinition(self, ctx:SpeakQlParser.ColumnDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#nullColumnConstraint.
    def visitNullColumnConstraint(self, ctx:SpeakQlParser.NullColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#defaultColumnConstraint.
    def visitDefaultColumnConstraint(self, ctx:SpeakQlParser.DefaultColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#visibilityColumnConstraint.
    def visitVisibilityColumnConstraint(self, ctx:SpeakQlParser.VisibilityColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#autoIncrementColumnConstraint.
    def visitAutoIncrementColumnConstraint(self, ctx:SpeakQlParser.AutoIncrementColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#primaryKeyColumnConstraint.
    def visitPrimaryKeyColumnConstraint(self, ctx:SpeakQlParser.PrimaryKeyColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#uniqueKeyColumnConstraint.
    def visitUniqueKeyColumnConstraint(self, ctx:SpeakQlParser.UniqueKeyColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#commentColumnConstraint.
    def visitCommentColumnConstraint(self, ctx:SpeakQlParser.CommentColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#formatColumnConstraint.
    def visitFormatColumnConstraint(self, ctx:SpeakQlParser.FormatColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#storageColumnConstraint.
    def visitStorageColumnConstraint(self, ctx:SpeakQlParser.StorageColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#referenceColumnConstraint.
    def visitReferenceColumnConstraint(self, ctx:SpeakQlParser.ReferenceColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#collateColumnConstraint.
    def visitCollateColumnConstraint(self, ctx:SpeakQlParser.CollateColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#generatedColumnConstraint.
    def visitGeneratedColumnConstraint(self, ctx:SpeakQlParser.GeneratedColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#serialDefaultColumnConstraint.
    def visitSerialDefaultColumnConstraint(self, ctx:SpeakQlParser.SerialDefaultColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#checkColumnConstraint.
    def visitCheckColumnConstraint(self, ctx:SpeakQlParser.CheckColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#primaryKeyTableConstraint.
    def visitPrimaryKeyTableConstraint(self, ctx:SpeakQlParser.PrimaryKeyTableConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#uniqueKeyTableConstraint.
    def visitUniqueKeyTableConstraint(self, ctx:SpeakQlParser.UniqueKeyTableConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#foreignKeyTableConstraint.
    def visitForeignKeyTableConstraint(self, ctx:SpeakQlParser.ForeignKeyTableConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#checkTableConstraint.
    def visitCheckTableConstraint(self, ctx:SpeakQlParser.CheckTableConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#referenceDefinition.
    def visitReferenceDefinition(self, ctx:SpeakQlParser.ReferenceDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#referenceAction.
    def visitReferenceAction(self, ctx:SpeakQlParser.ReferenceActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#referenceControlType.
    def visitReferenceControlType(self, ctx:SpeakQlParser.ReferenceControlTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#simpleIndexDeclaration.
    def visitSimpleIndexDeclaration(self, ctx:SpeakQlParser.SimpleIndexDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#specialIndexDeclaration.
    def visitSpecialIndexDeclaration(self, ctx:SpeakQlParser.SpecialIndexDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableOptionEngine.
    def visitTableOptionEngine(self, ctx:SpeakQlParser.TableOptionEngineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableOptionAutoIncrement.
    def visitTableOptionAutoIncrement(self, ctx:SpeakQlParser.TableOptionAutoIncrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableOptionAverage.
    def visitTableOptionAverage(self, ctx:SpeakQlParser.TableOptionAverageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableOptionCharset.
    def visitTableOptionCharset(self, ctx:SpeakQlParser.TableOptionCharsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableOptionChecksum.
    def visitTableOptionChecksum(self, ctx:SpeakQlParser.TableOptionChecksumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableOptionCollate.
    def visitTableOptionCollate(self, ctx:SpeakQlParser.TableOptionCollateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableOptionComment.
    def visitTableOptionComment(self, ctx:SpeakQlParser.TableOptionCommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableOptionCompression.
    def visitTableOptionCompression(self, ctx:SpeakQlParser.TableOptionCompressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableOptionConnection.
    def visitTableOptionConnection(self, ctx:SpeakQlParser.TableOptionConnectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableOptionDataDirectory.
    def visitTableOptionDataDirectory(self, ctx:SpeakQlParser.TableOptionDataDirectoryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableOptionDelay.
    def visitTableOptionDelay(self, ctx:SpeakQlParser.TableOptionDelayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableOptionEncryption.
    def visitTableOptionEncryption(self, ctx:SpeakQlParser.TableOptionEncryptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableOptionIndexDirectory.
    def visitTableOptionIndexDirectory(self, ctx:SpeakQlParser.TableOptionIndexDirectoryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableOptionInsertMethod.
    def visitTableOptionInsertMethod(self, ctx:SpeakQlParser.TableOptionInsertMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableOptionKeyBlockSize.
    def visitTableOptionKeyBlockSize(self, ctx:SpeakQlParser.TableOptionKeyBlockSizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableOptionMaxRows.
    def visitTableOptionMaxRows(self, ctx:SpeakQlParser.TableOptionMaxRowsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableOptionMinRows.
    def visitTableOptionMinRows(self, ctx:SpeakQlParser.TableOptionMinRowsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableOptionPackKeys.
    def visitTableOptionPackKeys(self, ctx:SpeakQlParser.TableOptionPackKeysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableOptionPassword.
    def visitTableOptionPassword(self, ctx:SpeakQlParser.TableOptionPasswordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableOptionRowFormat.
    def visitTableOptionRowFormat(self, ctx:SpeakQlParser.TableOptionRowFormatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableOptionRecalculation.
    def visitTableOptionRecalculation(self, ctx:SpeakQlParser.TableOptionRecalculationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableOptionPersistent.
    def visitTableOptionPersistent(self, ctx:SpeakQlParser.TableOptionPersistentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableOptionSamplePage.
    def visitTableOptionSamplePage(self, ctx:SpeakQlParser.TableOptionSamplePageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableOptionTablespace.
    def visitTableOptionTablespace(self, ctx:SpeakQlParser.TableOptionTablespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableOptionTableType.
    def visitTableOptionTableType(self, ctx:SpeakQlParser.TableOptionTableTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableOptionUnion.
    def visitTableOptionUnion(self, ctx:SpeakQlParser.TableOptionUnionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableType.
    def visitTableType(self, ctx:SpeakQlParser.TableTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tablespaceStorage.
    def visitTablespaceStorage(self, ctx:SpeakQlParser.TablespaceStorageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#partitionDefinitions.
    def visitPartitionDefinitions(self, ctx:SpeakQlParser.PartitionDefinitionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#partitionFunctionHash.
    def visitPartitionFunctionHash(self, ctx:SpeakQlParser.PartitionFunctionHashContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#partitionFunctionKey.
    def visitPartitionFunctionKey(self, ctx:SpeakQlParser.PartitionFunctionKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#partitionFunctionRange.
    def visitPartitionFunctionRange(self, ctx:SpeakQlParser.PartitionFunctionRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#partitionFunctionList.
    def visitPartitionFunctionList(self, ctx:SpeakQlParser.PartitionFunctionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#subPartitionFunctionHash.
    def visitSubPartitionFunctionHash(self, ctx:SpeakQlParser.SubPartitionFunctionHashContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#subPartitionFunctionKey.
    def visitSubPartitionFunctionKey(self, ctx:SpeakQlParser.SubPartitionFunctionKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#partitionComparison.
    def visitPartitionComparison(self, ctx:SpeakQlParser.PartitionComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#partitionListAtom.
    def visitPartitionListAtom(self, ctx:SpeakQlParser.PartitionListAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#partitionListVector.
    def visitPartitionListVector(self, ctx:SpeakQlParser.PartitionListVectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#partitionSimple.
    def visitPartitionSimple(self, ctx:SpeakQlParser.PartitionSimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#partitionDefinerAtom.
    def visitPartitionDefinerAtom(self, ctx:SpeakQlParser.PartitionDefinerAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#partitionDefinerVector.
    def visitPartitionDefinerVector(self, ctx:SpeakQlParser.PartitionDefinerVectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#subpartitionDefinition.
    def visitSubpartitionDefinition(self, ctx:SpeakQlParser.SubpartitionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#partitionOptionEngine.
    def visitPartitionOptionEngine(self, ctx:SpeakQlParser.PartitionOptionEngineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#partitionOptionComment.
    def visitPartitionOptionComment(self, ctx:SpeakQlParser.PartitionOptionCommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#partitionOptionDataDirectory.
    def visitPartitionOptionDataDirectory(self, ctx:SpeakQlParser.PartitionOptionDataDirectoryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#partitionOptionIndexDirectory.
    def visitPartitionOptionIndexDirectory(self, ctx:SpeakQlParser.PartitionOptionIndexDirectoryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#partitionOptionMaxRows.
    def visitPartitionOptionMaxRows(self, ctx:SpeakQlParser.PartitionOptionMaxRowsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#partitionOptionMinRows.
    def visitPartitionOptionMinRows(self, ctx:SpeakQlParser.PartitionOptionMinRowsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#partitionOptionTablespace.
    def visitPartitionOptionTablespace(self, ctx:SpeakQlParser.PartitionOptionTablespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#partitionOptionNodeGroup.
    def visitPartitionOptionNodeGroup(self, ctx:SpeakQlParser.PartitionOptionNodeGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterSimpleDatabase.
    def visitAlterSimpleDatabase(self, ctx:SpeakQlParser.AlterSimpleDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterUpgradeName.
    def visitAlterUpgradeName(self, ctx:SpeakQlParser.AlterUpgradeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterEvent.
    def visitAlterEvent(self, ctx:SpeakQlParser.AlterEventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterFunction.
    def visitAlterFunction(self, ctx:SpeakQlParser.AlterFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterInstance.
    def visitAlterInstance(self, ctx:SpeakQlParser.AlterInstanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterLogfileGroup.
    def visitAlterLogfileGroup(self, ctx:SpeakQlParser.AlterLogfileGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterProcedure.
    def visitAlterProcedure(self, ctx:SpeakQlParser.AlterProcedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterServer.
    def visitAlterServer(self, ctx:SpeakQlParser.AlterServerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterTable.
    def visitAlterTable(self, ctx:SpeakQlParser.AlterTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterTablespace.
    def visitAlterTablespace(self, ctx:SpeakQlParser.AlterTablespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterView.
    def visitAlterView(self, ctx:SpeakQlParser.AlterViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByTableOption.
    def visitAlterByTableOption(self, ctx:SpeakQlParser.AlterByTableOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByAddColumn.
    def visitAlterByAddColumn(self, ctx:SpeakQlParser.AlterByAddColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByAddColumns.
    def visitAlterByAddColumns(self, ctx:SpeakQlParser.AlterByAddColumnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByAddIndex.
    def visitAlterByAddIndex(self, ctx:SpeakQlParser.AlterByAddIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByAddPrimaryKey.
    def visitAlterByAddPrimaryKey(self, ctx:SpeakQlParser.AlterByAddPrimaryKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByAddUniqueKey.
    def visitAlterByAddUniqueKey(self, ctx:SpeakQlParser.AlterByAddUniqueKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByAddSpecialIndex.
    def visitAlterByAddSpecialIndex(self, ctx:SpeakQlParser.AlterByAddSpecialIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByAddForeignKey.
    def visitAlterByAddForeignKey(self, ctx:SpeakQlParser.AlterByAddForeignKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByAddCheckTableConstraint.
    def visitAlterByAddCheckTableConstraint(self, ctx:SpeakQlParser.AlterByAddCheckTableConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterBySetAlgorithm.
    def visitAlterBySetAlgorithm(self, ctx:SpeakQlParser.AlterBySetAlgorithmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByChangeDefault.
    def visitAlterByChangeDefault(self, ctx:SpeakQlParser.AlterByChangeDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByChangeColumn.
    def visitAlterByChangeColumn(self, ctx:SpeakQlParser.AlterByChangeColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByRenameColumn.
    def visitAlterByRenameColumn(self, ctx:SpeakQlParser.AlterByRenameColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByLock.
    def visitAlterByLock(self, ctx:SpeakQlParser.AlterByLockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByModifyColumn.
    def visitAlterByModifyColumn(self, ctx:SpeakQlParser.AlterByModifyColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByDropColumn.
    def visitAlterByDropColumn(self, ctx:SpeakQlParser.AlterByDropColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByDropConstraintCheck.
    def visitAlterByDropConstraintCheck(self, ctx:SpeakQlParser.AlterByDropConstraintCheckContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByDropPrimaryKey.
    def visitAlterByDropPrimaryKey(self, ctx:SpeakQlParser.AlterByDropPrimaryKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByRenameIndex.
    def visitAlterByRenameIndex(self, ctx:SpeakQlParser.AlterByRenameIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByAlterIndexVisibility.
    def visitAlterByAlterIndexVisibility(self, ctx:SpeakQlParser.AlterByAlterIndexVisibilityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByDropIndex.
    def visitAlterByDropIndex(self, ctx:SpeakQlParser.AlterByDropIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByDropForeignKey.
    def visitAlterByDropForeignKey(self, ctx:SpeakQlParser.AlterByDropForeignKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByDisableKeys.
    def visitAlterByDisableKeys(self, ctx:SpeakQlParser.AlterByDisableKeysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByEnableKeys.
    def visitAlterByEnableKeys(self, ctx:SpeakQlParser.AlterByEnableKeysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByRename.
    def visitAlterByRename(self, ctx:SpeakQlParser.AlterByRenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByOrder.
    def visitAlterByOrder(self, ctx:SpeakQlParser.AlterByOrderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByConvertCharset.
    def visitAlterByConvertCharset(self, ctx:SpeakQlParser.AlterByConvertCharsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByDefaultCharset.
    def visitAlterByDefaultCharset(self, ctx:SpeakQlParser.AlterByDefaultCharsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByDiscardTablespace.
    def visitAlterByDiscardTablespace(self, ctx:SpeakQlParser.AlterByDiscardTablespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByImportTablespace.
    def visitAlterByImportTablespace(self, ctx:SpeakQlParser.AlterByImportTablespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByForce.
    def visitAlterByForce(self, ctx:SpeakQlParser.AlterByForceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByValidate.
    def visitAlterByValidate(self, ctx:SpeakQlParser.AlterByValidateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByAddPartition.
    def visitAlterByAddPartition(self, ctx:SpeakQlParser.AlterByAddPartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByDropPartition.
    def visitAlterByDropPartition(self, ctx:SpeakQlParser.AlterByDropPartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByDiscardPartition.
    def visitAlterByDiscardPartition(self, ctx:SpeakQlParser.AlterByDiscardPartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByImportPartition.
    def visitAlterByImportPartition(self, ctx:SpeakQlParser.AlterByImportPartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByTruncatePartition.
    def visitAlterByTruncatePartition(self, ctx:SpeakQlParser.AlterByTruncatePartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByCoalescePartition.
    def visitAlterByCoalescePartition(self, ctx:SpeakQlParser.AlterByCoalescePartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByReorganizePartition.
    def visitAlterByReorganizePartition(self, ctx:SpeakQlParser.AlterByReorganizePartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByExchangePartition.
    def visitAlterByExchangePartition(self, ctx:SpeakQlParser.AlterByExchangePartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByAnalyzePartition.
    def visitAlterByAnalyzePartition(self, ctx:SpeakQlParser.AlterByAnalyzePartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByCheckPartition.
    def visitAlterByCheckPartition(self, ctx:SpeakQlParser.AlterByCheckPartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByOptimizePartition.
    def visitAlterByOptimizePartition(self, ctx:SpeakQlParser.AlterByOptimizePartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByRebuildPartition.
    def visitAlterByRebuildPartition(self, ctx:SpeakQlParser.AlterByRebuildPartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByRepairPartition.
    def visitAlterByRepairPartition(self, ctx:SpeakQlParser.AlterByRepairPartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByRemovePartitioning.
    def visitAlterByRemovePartitioning(self, ctx:SpeakQlParser.AlterByRemovePartitioningContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterByUpgradePartitioning.
    def visitAlterByUpgradePartitioning(self, ctx:SpeakQlParser.AlterByUpgradePartitioningContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#dropDatabase.
    def visitDropDatabase(self, ctx:SpeakQlParser.DropDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#dropEvent.
    def visitDropEvent(self, ctx:SpeakQlParser.DropEventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#dropIndex.
    def visitDropIndex(self, ctx:SpeakQlParser.DropIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#dropLogfileGroup.
    def visitDropLogfileGroup(self, ctx:SpeakQlParser.DropLogfileGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#dropProcedure.
    def visitDropProcedure(self, ctx:SpeakQlParser.DropProcedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#dropFunction.
    def visitDropFunction(self, ctx:SpeakQlParser.DropFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#dropServer.
    def visitDropServer(self, ctx:SpeakQlParser.DropServerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#dropTable.
    def visitDropTable(self, ctx:SpeakQlParser.DropTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#dropTablespace.
    def visitDropTablespace(self, ctx:SpeakQlParser.DropTablespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#dropTrigger.
    def visitDropTrigger(self, ctx:SpeakQlParser.DropTriggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#dropView.
    def visitDropView(self, ctx:SpeakQlParser.DropViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#renameTable.
    def visitRenameTable(self, ctx:SpeakQlParser.RenameTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#renameTableClause.
    def visitRenameTableClause(self, ctx:SpeakQlParser.RenameTableClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#truncateTable.
    def visitTruncateTable(self, ctx:SpeakQlParser.TruncateTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#callStatement.
    def visitCallStatement(self, ctx:SpeakQlParser.CallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#deleteStatement.
    def visitDeleteStatement(self, ctx:SpeakQlParser.DeleteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#doStatement.
    def visitDoStatement(self, ctx:SpeakQlParser.DoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#handlerStatement.
    def visitHandlerStatement(self, ctx:SpeakQlParser.HandlerStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#insertStatement.
    def visitInsertStatement(self, ctx:SpeakQlParser.InsertStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#loadDataStatement.
    def visitLoadDataStatement(self, ctx:SpeakQlParser.LoadDataStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#loadXmlStatement.
    def visitLoadXmlStatement(self, ctx:SpeakQlParser.LoadXmlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#replaceStatement.
    def visitReplaceStatement(self, ctx:SpeakQlParser.ReplaceStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#simpleSelect.
    def visitSimpleSelect(self, ctx:SpeakQlParser.SimpleSelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#parenthesisSelect.
    def visitParenthesisSelect(self, ctx:SpeakQlParser.ParenthesisSelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#unionSelect.
    def visitUnionSelect(self, ctx:SpeakQlParser.UnionSelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#unionParenthesisSelect.
    def visitUnionParenthesisSelect(self, ctx:SpeakQlParser.UnionParenthesisSelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#updateStatement.
    def visitUpdateStatement(self, ctx:SpeakQlParser.UpdateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#insertStatementValue.
    def visitInsertStatementValue(self, ctx:SpeakQlParser.InsertStatementValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#updatedElement.
    def visitUpdatedElement(self, ctx:SpeakQlParser.UpdatedElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#assignmentField.
    def visitAssignmentField(self, ctx:SpeakQlParser.AssignmentFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#lockClause.
    def visitLockClause(self, ctx:SpeakQlParser.LockClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#singleDeleteStatement.
    def visitSingleDeleteStatement(self, ctx:SpeakQlParser.SingleDeleteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#multipleDeleteStatement.
    def visitMultipleDeleteStatement(self, ctx:SpeakQlParser.MultipleDeleteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#handlerOpenStatement.
    def visitHandlerOpenStatement(self, ctx:SpeakQlParser.HandlerOpenStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#handlerReadIndexStatement.
    def visitHandlerReadIndexStatement(self, ctx:SpeakQlParser.HandlerReadIndexStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#handlerReadStatement.
    def visitHandlerReadStatement(self, ctx:SpeakQlParser.HandlerReadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#handlerCloseStatement.
    def visitHandlerCloseStatement(self, ctx:SpeakQlParser.HandlerCloseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#singleUpdateStatement.
    def visitSingleUpdateStatement(self, ctx:SpeakQlParser.SingleUpdateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#multipleUpdateStatement.
    def visitMultipleUpdateStatement(self, ctx:SpeakQlParser.MultipleUpdateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#orderByClause.
    def visitOrderByClause(self, ctx:SpeakQlParser.OrderByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#orderByExpression.
    def visitOrderByExpression(self, ctx:SpeakQlParser.OrderByExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableSources.
    def visitTableSources(self, ctx:SpeakQlParser.TableSourcesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableSourceBase.
    def visitTableSourceBase(self, ctx:SpeakQlParser.TableSourceBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableSourceNested.
    def visitTableSourceNested(self, ctx:SpeakQlParser.TableSourceNestedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#atomTableItem.
    def visitAtomTableItem(self, ctx:SpeakQlParser.AtomTableItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#subqueryTableItem.
    def visitSubqueryTableItem(self, ctx:SpeakQlParser.SubqueryTableItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableSourcesItem.
    def visitTableSourcesItem(self, ctx:SpeakQlParser.TableSourcesItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#indexHint.
    def visitIndexHint(self, ctx:SpeakQlParser.IndexHintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#indexHintType.
    def visitIndexHintType(self, ctx:SpeakQlParser.IndexHintTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#innerJoin.
    def visitInnerJoin(self, ctx:SpeakQlParser.InnerJoinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#straightJoin.
    def visitStraightJoin(self, ctx:SpeakQlParser.StraightJoinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#outerJoin.
    def visitOuterJoin(self, ctx:SpeakQlParser.OuterJoinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#naturalJoin.
    def visitNaturalJoin(self, ctx:SpeakQlParser.NaturalJoinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#joinKeyword.
    def visitJoinKeyword(self, ctx:SpeakQlParser.JoinKeywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#queryExpression.
    def visitQueryExpression(self, ctx:SpeakQlParser.QueryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#queryExpressionNointo.
    def visitQueryExpressionNointo(self, ctx:SpeakQlParser.QueryExpressionNointoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#querySpecification.
    def visitQuerySpecification(self, ctx:SpeakQlParser.QuerySpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#selectModifierExpression.
    def visitSelectModifierExpression(self, ctx:SpeakQlParser.SelectModifierExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#selectExpression.
    def visitSelectExpression(self, ctx:SpeakQlParser.SelectExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableExpression.
    def visitTableExpression(self, ctx:SpeakQlParser.TableExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#selectClause.
    def visitSelectClause(self, ctx:SpeakQlParser.SelectClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#selectKeyword.
    def visitSelectKeyword(self, ctx:SpeakQlParser.SelectKeywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#querySpecificationNointo.
    def visitQuerySpecificationNointo(self, ctx:SpeakQlParser.QuerySpecificationNointoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#unionParenthesis.
    def visitUnionParenthesis(self, ctx:SpeakQlParser.UnionParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#unionStatement.
    def visitUnionStatement(self, ctx:SpeakQlParser.UnionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#selectSpec.
    def visitSelectSpec(self, ctx:SpeakQlParser.SelectSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#selectElements.
    def visitSelectElements(self, ctx:SpeakQlParser.SelectElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#selectElementDelimiter.
    def visitSelectElementDelimiter(self, ctx:SpeakQlParser.SelectElementDelimiterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#selectStarElement.
    def visitSelectStarElement(self, ctx:SpeakQlParser.SelectStarElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#selectColumnElement.
    def visitSelectColumnElement(self, ctx:SpeakQlParser.SelectColumnElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#selectFunctionElement.
    def visitSelectFunctionElement(self, ctx:SpeakQlParser.SelectFunctionElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#selectExpressionElement.
    def visitSelectExpressionElement(self, ctx:SpeakQlParser.SelectExpressionElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#selectIntoVariables.
    def visitSelectIntoVariables(self, ctx:SpeakQlParser.SelectIntoVariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#selectIntoDumpFile.
    def visitSelectIntoDumpFile(self, ctx:SpeakQlParser.SelectIntoDumpFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#selectIntoTextFile.
    def visitSelectIntoTextFile(self, ctx:SpeakQlParser.SelectIntoTextFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#selectFieldsInto.
    def visitSelectFieldsInto(self, ctx:SpeakQlParser.SelectFieldsIntoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#selectLinesInto.
    def visitSelectLinesInto(self, ctx:SpeakQlParser.SelectLinesIntoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#fromClause.
    def visitFromClause(self, ctx:SpeakQlParser.FromClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#fromKeyword.
    def visitFromKeyword(self, ctx:SpeakQlParser.FromKeywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#groupByClause.
    def visitGroupByClause(self, ctx:SpeakQlParser.GroupByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#havingClause.
    def visitHavingClause(self, ctx:SpeakQlParser.HavingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#windowClause.
    def visitWindowClause(self, ctx:SpeakQlParser.WindowClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#groupByItem.
    def visitGroupByItem(self, ctx:SpeakQlParser.GroupByItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#limitClause.
    def visitLimitClause(self, ctx:SpeakQlParser.LimitClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#limitClauseAtom.
    def visitLimitClauseAtom(self, ctx:SpeakQlParser.LimitClauseAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#startTransaction.
    def visitStartTransaction(self, ctx:SpeakQlParser.StartTransactionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#beginWork.
    def visitBeginWork(self, ctx:SpeakQlParser.BeginWorkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#commitWork.
    def visitCommitWork(self, ctx:SpeakQlParser.CommitWorkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#rollbackWork.
    def visitRollbackWork(self, ctx:SpeakQlParser.RollbackWorkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#savepointStatement.
    def visitSavepointStatement(self, ctx:SpeakQlParser.SavepointStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#rollbackStatement.
    def visitRollbackStatement(self, ctx:SpeakQlParser.RollbackStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#releaseStatement.
    def visitReleaseStatement(self, ctx:SpeakQlParser.ReleaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#lockTables.
    def visitLockTables(self, ctx:SpeakQlParser.LockTablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#unlockTables.
    def visitUnlockTables(self, ctx:SpeakQlParser.UnlockTablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#setAutocommitStatement.
    def visitSetAutocommitStatement(self, ctx:SpeakQlParser.SetAutocommitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#setTransactionStatement.
    def visitSetTransactionStatement(self, ctx:SpeakQlParser.SetTransactionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#transactionMode.
    def visitTransactionMode(self, ctx:SpeakQlParser.TransactionModeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#lockTableElement.
    def visitLockTableElement(self, ctx:SpeakQlParser.LockTableElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#lockAction.
    def visitLockAction(self, ctx:SpeakQlParser.LockActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#transactionOption.
    def visitTransactionOption(self, ctx:SpeakQlParser.TransactionOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#transactionLevel.
    def visitTransactionLevel(self, ctx:SpeakQlParser.TransactionLevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#changeMaster.
    def visitChangeMaster(self, ctx:SpeakQlParser.ChangeMasterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#changeReplicationFilter.
    def visitChangeReplicationFilter(self, ctx:SpeakQlParser.ChangeReplicationFilterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#purgeBinaryLogs.
    def visitPurgeBinaryLogs(self, ctx:SpeakQlParser.PurgeBinaryLogsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#resetMaster.
    def visitResetMaster(self, ctx:SpeakQlParser.ResetMasterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#resetSlave.
    def visitResetSlave(self, ctx:SpeakQlParser.ResetSlaveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#startSlave.
    def visitStartSlave(self, ctx:SpeakQlParser.StartSlaveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#stopSlave.
    def visitStopSlave(self, ctx:SpeakQlParser.StopSlaveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#startGroupReplication.
    def visitStartGroupReplication(self, ctx:SpeakQlParser.StartGroupReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#stopGroupReplication.
    def visitStopGroupReplication(self, ctx:SpeakQlParser.StopGroupReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#masterStringOption.
    def visitMasterStringOption(self, ctx:SpeakQlParser.MasterStringOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#masterDecimalOption.
    def visitMasterDecimalOption(self, ctx:SpeakQlParser.MasterDecimalOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#masterBoolOption.
    def visitMasterBoolOption(self, ctx:SpeakQlParser.MasterBoolOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#masterRealOption.
    def visitMasterRealOption(self, ctx:SpeakQlParser.MasterRealOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#masterUidListOption.
    def visitMasterUidListOption(self, ctx:SpeakQlParser.MasterUidListOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#stringMasterOption.
    def visitStringMasterOption(self, ctx:SpeakQlParser.StringMasterOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#decimalMasterOption.
    def visitDecimalMasterOption(self, ctx:SpeakQlParser.DecimalMasterOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#boolMasterOption.
    def visitBoolMasterOption(self, ctx:SpeakQlParser.BoolMasterOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#channelOption.
    def visitChannelOption(self, ctx:SpeakQlParser.ChannelOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#doDbReplication.
    def visitDoDbReplication(self, ctx:SpeakQlParser.DoDbReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#ignoreDbReplication.
    def visitIgnoreDbReplication(self, ctx:SpeakQlParser.IgnoreDbReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#doTableReplication.
    def visitDoTableReplication(self, ctx:SpeakQlParser.DoTableReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#ignoreTableReplication.
    def visitIgnoreTableReplication(self, ctx:SpeakQlParser.IgnoreTableReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#wildDoTableReplication.
    def visitWildDoTableReplication(self, ctx:SpeakQlParser.WildDoTableReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#wildIgnoreTableReplication.
    def visitWildIgnoreTableReplication(self, ctx:SpeakQlParser.WildIgnoreTableReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#rewriteDbReplication.
    def visitRewriteDbReplication(self, ctx:SpeakQlParser.RewriteDbReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tablePair.
    def visitTablePair(self, ctx:SpeakQlParser.TablePairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#threadType.
    def visitThreadType(self, ctx:SpeakQlParser.ThreadTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#gtidsUntilOption.
    def visitGtidsUntilOption(self, ctx:SpeakQlParser.GtidsUntilOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#masterLogUntilOption.
    def visitMasterLogUntilOption(self, ctx:SpeakQlParser.MasterLogUntilOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#relayLogUntilOption.
    def visitRelayLogUntilOption(self, ctx:SpeakQlParser.RelayLogUntilOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#sqlGapsUntilOption.
    def visitSqlGapsUntilOption(self, ctx:SpeakQlParser.SqlGapsUntilOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#userConnectionOption.
    def visitUserConnectionOption(self, ctx:SpeakQlParser.UserConnectionOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#passwordConnectionOption.
    def visitPasswordConnectionOption(self, ctx:SpeakQlParser.PasswordConnectionOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#defaultAuthConnectionOption.
    def visitDefaultAuthConnectionOption(self, ctx:SpeakQlParser.DefaultAuthConnectionOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#pluginDirConnectionOption.
    def visitPluginDirConnectionOption(self, ctx:SpeakQlParser.PluginDirConnectionOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#gtuidSet.
    def visitGtuidSet(self, ctx:SpeakQlParser.GtuidSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#xaStartTransaction.
    def visitXaStartTransaction(self, ctx:SpeakQlParser.XaStartTransactionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#xaEndTransaction.
    def visitXaEndTransaction(self, ctx:SpeakQlParser.XaEndTransactionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#xaPrepareStatement.
    def visitXaPrepareStatement(self, ctx:SpeakQlParser.XaPrepareStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#xaCommitWork.
    def visitXaCommitWork(self, ctx:SpeakQlParser.XaCommitWorkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#xaRollbackWork.
    def visitXaRollbackWork(self, ctx:SpeakQlParser.XaRollbackWorkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#xaRecoverWork.
    def visitXaRecoverWork(self, ctx:SpeakQlParser.XaRecoverWorkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#prepareStatement.
    def visitPrepareStatement(self, ctx:SpeakQlParser.PrepareStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#executeStatement.
    def visitExecuteStatement(self, ctx:SpeakQlParser.ExecuteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#deallocatePrepare.
    def visitDeallocatePrepare(self, ctx:SpeakQlParser.DeallocatePrepareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#routineBody.
    def visitRoutineBody(self, ctx:SpeakQlParser.RoutineBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#blockStatement.
    def visitBlockStatement(self, ctx:SpeakQlParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#caseStatement.
    def visitCaseStatement(self, ctx:SpeakQlParser.CaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#ifStatement.
    def visitIfStatement(self, ctx:SpeakQlParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#iterateStatement.
    def visitIterateStatement(self, ctx:SpeakQlParser.IterateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#leaveStatement.
    def visitLeaveStatement(self, ctx:SpeakQlParser.LeaveStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#loopStatement.
    def visitLoopStatement(self, ctx:SpeakQlParser.LoopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#repeatStatement.
    def visitRepeatStatement(self, ctx:SpeakQlParser.RepeatStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#returnStatement.
    def visitReturnStatement(self, ctx:SpeakQlParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#whileStatement.
    def visitWhileStatement(self, ctx:SpeakQlParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#CloseCursor.
    def visitCloseCursor(self, ctx:SpeakQlParser.CloseCursorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#FetchCursor.
    def visitFetchCursor(self, ctx:SpeakQlParser.FetchCursorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#OpenCursor.
    def visitOpenCursor(self, ctx:SpeakQlParser.OpenCursorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#declareVariable.
    def visitDeclareVariable(self, ctx:SpeakQlParser.DeclareVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#declareCondition.
    def visitDeclareCondition(self, ctx:SpeakQlParser.DeclareConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#declareCursor.
    def visitDeclareCursor(self, ctx:SpeakQlParser.DeclareCursorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#declareHandler.
    def visitDeclareHandler(self, ctx:SpeakQlParser.DeclareHandlerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#handlerConditionCode.
    def visitHandlerConditionCode(self, ctx:SpeakQlParser.HandlerConditionCodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#handlerConditionState.
    def visitHandlerConditionState(self, ctx:SpeakQlParser.HandlerConditionStateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#handlerConditionName.
    def visitHandlerConditionName(self, ctx:SpeakQlParser.HandlerConditionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#handlerConditionWarning.
    def visitHandlerConditionWarning(self, ctx:SpeakQlParser.HandlerConditionWarningContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#handlerConditionNotfound.
    def visitHandlerConditionNotfound(self, ctx:SpeakQlParser.HandlerConditionNotfoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#handlerConditionException.
    def visitHandlerConditionException(self, ctx:SpeakQlParser.HandlerConditionExceptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#procedureSqlStatement.
    def visitProcedureSqlStatement(self, ctx:SpeakQlParser.ProcedureSqlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#caseAlternative.
    def visitCaseAlternative(self, ctx:SpeakQlParser.CaseAlternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#elifAlternative.
    def visitElifAlternative(self, ctx:SpeakQlParser.ElifAlternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterUserMysqlV56.
    def visitAlterUserMysqlV56(self, ctx:SpeakQlParser.AlterUserMysqlV56Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#alterUserMysqlV57.
    def visitAlterUserMysqlV57(self, ctx:SpeakQlParser.AlterUserMysqlV57Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#createUserMysqlV56.
    def visitCreateUserMysqlV56(self, ctx:SpeakQlParser.CreateUserMysqlV56Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#createUserMysqlV57.
    def visitCreateUserMysqlV57(self, ctx:SpeakQlParser.CreateUserMysqlV57Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#dropUser.
    def visitDropUser(self, ctx:SpeakQlParser.DropUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#grantStatement.
    def visitGrantStatement(self, ctx:SpeakQlParser.GrantStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#roleOption.
    def visitRoleOption(self, ctx:SpeakQlParser.RoleOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#grantProxy.
    def visitGrantProxy(self, ctx:SpeakQlParser.GrantProxyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#renameUser.
    def visitRenameUser(self, ctx:SpeakQlParser.RenameUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#detailRevoke.
    def visitDetailRevoke(self, ctx:SpeakQlParser.DetailRevokeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#shortRevoke.
    def visitShortRevoke(self, ctx:SpeakQlParser.ShortRevokeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#roleRevoke.
    def visitRoleRevoke(self, ctx:SpeakQlParser.RoleRevokeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#revokeProxy.
    def visitRevokeProxy(self, ctx:SpeakQlParser.RevokeProxyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#setPasswordStatement.
    def visitSetPasswordStatement(self, ctx:SpeakQlParser.SetPasswordStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#userSpecification.
    def visitUserSpecification(self, ctx:SpeakQlParser.UserSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#passwordAuthOption.
    def visitPasswordAuthOption(self, ctx:SpeakQlParser.PasswordAuthOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#stringAuthOption.
    def visitStringAuthOption(self, ctx:SpeakQlParser.StringAuthOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#hashAuthOption.
    def visitHashAuthOption(self, ctx:SpeakQlParser.HashAuthOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#simpleAuthOption.
    def visitSimpleAuthOption(self, ctx:SpeakQlParser.SimpleAuthOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tlsOption.
    def visitTlsOption(self, ctx:SpeakQlParser.TlsOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#userResourceOption.
    def visitUserResourceOption(self, ctx:SpeakQlParser.UserResourceOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#userPasswordOption.
    def visitUserPasswordOption(self, ctx:SpeakQlParser.UserPasswordOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#userLockOption.
    def visitUserLockOption(self, ctx:SpeakQlParser.UserLockOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#privelegeClause.
    def visitPrivelegeClause(self, ctx:SpeakQlParser.PrivelegeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#privilege.
    def visitPrivilege(self, ctx:SpeakQlParser.PrivilegeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#currentSchemaPriviLevel.
    def visitCurrentSchemaPriviLevel(self, ctx:SpeakQlParser.CurrentSchemaPriviLevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#globalPrivLevel.
    def visitGlobalPrivLevel(self, ctx:SpeakQlParser.GlobalPrivLevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#definiteSchemaPrivLevel.
    def visitDefiniteSchemaPrivLevel(self, ctx:SpeakQlParser.DefiniteSchemaPrivLevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#definiteFullTablePrivLevel.
    def visitDefiniteFullTablePrivLevel(self, ctx:SpeakQlParser.DefiniteFullTablePrivLevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#definiteFullTablePrivLevel2.
    def visitDefiniteFullTablePrivLevel2(self, ctx:SpeakQlParser.DefiniteFullTablePrivLevel2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#definiteTablePrivLevel.
    def visitDefiniteTablePrivLevel(self, ctx:SpeakQlParser.DefiniteTablePrivLevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#renameUserClause.
    def visitRenameUserClause(self, ctx:SpeakQlParser.RenameUserClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#analyzeTable.
    def visitAnalyzeTable(self, ctx:SpeakQlParser.AnalyzeTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#checkTable.
    def visitCheckTable(self, ctx:SpeakQlParser.CheckTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#checksumTable.
    def visitChecksumTable(self, ctx:SpeakQlParser.ChecksumTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#optimizeTable.
    def visitOptimizeTable(self, ctx:SpeakQlParser.OptimizeTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#repairTable.
    def visitRepairTable(self, ctx:SpeakQlParser.RepairTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#checkTableOption.
    def visitCheckTableOption(self, ctx:SpeakQlParser.CheckTableOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#createUdfunction.
    def visitCreateUdfunction(self, ctx:SpeakQlParser.CreateUdfunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#installPlugin.
    def visitInstallPlugin(self, ctx:SpeakQlParser.InstallPluginContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#uninstallPlugin.
    def visitUninstallPlugin(self, ctx:SpeakQlParser.UninstallPluginContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#setVariable.
    def visitSetVariable(self, ctx:SpeakQlParser.SetVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#setCharset.
    def visitSetCharset(self, ctx:SpeakQlParser.SetCharsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#setNames.
    def visitSetNames(self, ctx:SpeakQlParser.SetNamesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#setPassword.
    def visitSetPassword(self, ctx:SpeakQlParser.SetPasswordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#setTransaction.
    def visitSetTransaction(self, ctx:SpeakQlParser.SetTransactionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#setAutocommit.
    def visitSetAutocommit(self, ctx:SpeakQlParser.SetAutocommitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#setNewValueInsideTrigger.
    def visitSetNewValueInsideTrigger(self, ctx:SpeakQlParser.SetNewValueInsideTriggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#showMasterLogs.
    def visitShowMasterLogs(self, ctx:SpeakQlParser.ShowMasterLogsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#showLogEvents.
    def visitShowLogEvents(self, ctx:SpeakQlParser.ShowLogEventsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#showObjectFilter.
    def visitShowObjectFilter(self, ctx:SpeakQlParser.ShowObjectFilterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#showColumns.
    def visitShowColumns(self, ctx:SpeakQlParser.ShowColumnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#showCreateDb.
    def visitShowCreateDb(self, ctx:SpeakQlParser.ShowCreateDbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#showCreateFullIdObject.
    def visitShowCreateFullIdObject(self, ctx:SpeakQlParser.ShowCreateFullIdObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#showCreateUser.
    def visitShowCreateUser(self, ctx:SpeakQlParser.ShowCreateUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#showEngine.
    def visitShowEngine(self, ctx:SpeakQlParser.ShowEngineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#showGlobalInfo.
    def visitShowGlobalInfo(self, ctx:SpeakQlParser.ShowGlobalInfoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#showErrors.
    def visitShowErrors(self, ctx:SpeakQlParser.ShowErrorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#showCountErrors.
    def visitShowCountErrors(self, ctx:SpeakQlParser.ShowCountErrorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#showSchemaFilter.
    def visitShowSchemaFilter(self, ctx:SpeakQlParser.ShowSchemaFilterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#showRoutine.
    def visitShowRoutine(self, ctx:SpeakQlParser.ShowRoutineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#showGrants.
    def visitShowGrants(self, ctx:SpeakQlParser.ShowGrantsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#showIndexes.
    def visitShowIndexes(self, ctx:SpeakQlParser.ShowIndexesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#showOpenTables.
    def visitShowOpenTables(self, ctx:SpeakQlParser.ShowOpenTablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#showProfile.
    def visitShowProfile(self, ctx:SpeakQlParser.ShowProfileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#showSlaveStatus.
    def visitShowSlaveStatus(self, ctx:SpeakQlParser.ShowSlaveStatusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#variableClause.
    def visitVariableClause(self, ctx:SpeakQlParser.VariableClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#showCommonEntity.
    def visitShowCommonEntity(self, ctx:SpeakQlParser.ShowCommonEntityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#showFilter.
    def visitShowFilter(self, ctx:SpeakQlParser.ShowFilterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#showGlobalInfoClause.
    def visitShowGlobalInfoClause(self, ctx:SpeakQlParser.ShowGlobalInfoClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#showSchemaEntity.
    def visitShowSchemaEntity(self, ctx:SpeakQlParser.ShowSchemaEntityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#showProfileType.
    def visitShowProfileType(self, ctx:SpeakQlParser.ShowProfileTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#binlogStatement.
    def visitBinlogStatement(self, ctx:SpeakQlParser.BinlogStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#cacheIndexStatement.
    def visitCacheIndexStatement(self, ctx:SpeakQlParser.CacheIndexStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#flushStatement.
    def visitFlushStatement(self, ctx:SpeakQlParser.FlushStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#killStatement.
    def visitKillStatement(self, ctx:SpeakQlParser.KillStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#loadIndexIntoCache.
    def visitLoadIndexIntoCache(self, ctx:SpeakQlParser.LoadIndexIntoCacheContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#resetStatement.
    def visitResetStatement(self, ctx:SpeakQlParser.ResetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#shutdownStatement.
    def visitShutdownStatement(self, ctx:SpeakQlParser.ShutdownStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableIndexes.
    def visitTableIndexes(self, ctx:SpeakQlParser.TableIndexesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#simpleFlushOption.
    def visitSimpleFlushOption(self, ctx:SpeakQlParser.SimpleFlushOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#channelFlushOption.
    def visitChannelFlushOption(self, ctx:SpeakQlParser.ChannelFlushOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableFlushOption.
    def visitTableFlushOption(self, ctx:SpeakQlParser.TableFlushOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#flushTableOption.
    def visitFlushTableOption(self, ctx:SpeakQlParser.FlushTableOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#loadedTableIndexes.
    def visitLoadedTableIndexes(self, ctx:SpeakQlParser.LoadedTableIndexesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#simpleDescribeStatement.
    def visitSimpleDescribeStatement(self, ctx:SpeakQlParser.SimpleDescribeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#fullDescribeStatement.
    def visitFullDescribeStatement(self, ctx:SpeakQlParser.FullDescribeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#helpStatement.
    def visitHelpStatement(self, ctx:SpeakQlParser.HelpStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#useStatement.
    def visitUseStatement(self, ctx:SpeakQlParser.UseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#signalStatement.
    def visitSignalStatement(self, ctx:SpeakQlParser.SignalStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#resignalStatement.
    def visitResignalStatement(self, ctx:SpeakQlParser.ResignalStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#signalConditionInformation.
    def visitSignalConditionInformation(self, ctx:SpeakQlParser.SignalConditionInformationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#diagnosticsStatement.
    def visitDiagnosticsStatement(self, ctx:SpeakQlParser.DiagnosticsStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#diagnosticsConditionInformationName.
    def visitDiagnosticsConditionInformationName(self, ctx:SpeakQlParser.DiagnosticsConditionInformationNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#describeStatements.
    def visitDescribeStatements(self, ctx:SpeakQlParser.DescribeStatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#describeConnection.
    def visitDescribeConnection(self, ctx:SpeakQlParser.DescribeConnectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#fullId.
    def visitFullId(self, ctx:SpeakQlParser.FullIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tableName.
    def visitTableName(self, ctx:SpeakQlParser.TableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#fullColumnName.
    def visitFullColumnName(self, ctx:SpeakQlParser.FullColumnNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#indexColumnName.
    def visitIndexColumnName(self, ctx:SpeakQlParser.IndexColumnNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#userName.
    def visitUserName(self, ctx:SpeakQlParser.UserNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#mysqlVariable.
    def visitMysqlVariable(self, ctx:SpeakQlParser.MysqlVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#charsetName.
    def visitCharsetName(self, ctx:SpeakQlParser.CharsetNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#collationName.
    def visitCollationName(self, ctx:SpeakQlParser.CollationNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#engineName.
    def visitEngineName(self, ctx:SpeakQlParser.EngineNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#uuidSet.
    def visitUuidSet(self, ctx:SpeakQlParser.UuidSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#xid.
    def visitXid(self, ctx:SpeakQlParser.XidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#xuidStringId.
    def visitXuidStringId(self, ctx:SpeakQlParser.XuidStringIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#authPlugin.
    def visitAuthPlugin(self, ctx:SpeakQlParser.AuthPluginContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#uid.
    def visitUid(self, ctx:SpeakQlParser.UidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#simpleId.
    def visitSimpleId(self, ctx:SpeakQlParser.SimpleIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#dottedId.
    def visitDottedId(self, ctx:SpeakQlParser.DottedIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#decimalLiteral.
    def visitDecimalLiteral(self, ctx:SpeakQlParser.DecimalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#fileSizeLiteral.
    def visitFileSizeLiteral(self, ctx:SpeakQlParser.FileSizeLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#stringLiteral.
    def visitStringLiteral(self, ctx:SpeakQlParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#booleanLiteral.
    def visitBooleanLiteral(self, ctx:SpeakQlParser.BooleanLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#hexadecimalLiteral.
    def visitHexadecimalLiteral(self, ctx:SpeakQlParser.HexadecimalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#nullNotnull.
    def visitNullNotnull(self, ctx:SpeakQlParser.NullNotnullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#constant.
    def visitConstant(self, ctx:SpeakQlParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#stringDataType.
    def visitStringDataType(self, ctx:SpeakQlParser.StringDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#nationalStringDataType.
    def visitNationalStringDataType(self, ctx:SpeakQlParser.NationalStringDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#nationalVaryingStringDataType.
    def visitNationalVaryingStringDataType(self, ctx:SpeakQlParser.NationalVaryingStringDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#dimensionDataType.
    def visitDimensionDataType(self, ctx:SpeakQlParser.DimensionDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#simpleDataType.
    def visitSimpleDataType(self, ctx:SpeakQlParser.SimpleDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#collectionDataType.
    def visitCollectionDataType(self, ctx:SpeakQlParser.CollectionDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#spatialDataType.
    def visitSpatialDataType(self, ctx:SpeakQlParser.SpatialDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#longVarcharDataType.
    def visitLongVarcharDataType(self, ctx:SpeakQlParser.LongVarcharDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#longVarbinaryDataType.
    def visitLongVarbinaryDataType(self, ctx:SpeakQlParser.LongVarbinaryDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#collectionOptions.
    def visitCollectionOptions(self, ctx:SpeakQlParser.CollectionOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#convertedDataType.
    def visitConvertedDataType(self, ctx:SpeakQlParser.ConvertedDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#lengthOneDimension.
    def visitLengthOneDimension(self, ctx:SpeakQlParser.LengthOneDimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#lengthTwoDimension.
    def visitLengthTwoDimension(self, ctx:SpeakQlParser.LengthTwoDimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#lengthTwoOptionalDimension.
    def visitLengthTwoOptionalDimension(self, ctx:SpeakQlParser.LengthTwoOptionalDimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#uidList.
    def visitUidList(self, ctx:SpeakQlParser.UidListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#tables.
    def visitTables(self, ctx:SpeakQlParser.TablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#indexColumnNames.
    def visitIndexColumnNames(self, ctx:SpeakQlParser.IndexColumnNamesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#expressions.
    def visitExpressions(self, ctx:SpeakQlParser.ExpressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#expressionsWithDefaults.
    def visitExpressionsWithDefaults(self, ctx:SpeakQlParser.ExpressionsWithDefaultsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#constants.
    def visitConstants(self, ctx:SpeakQlParser.ConstantsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#simpleStrings.
    def visitSimpleStrings(self, ctx:SpeakQlParser.SimpleStringsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#userVariables.
    def visitUserVariables(self, ctx:SpeakQlParser.UserVariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#defaultValue.
    def visitDefaultValue(self, ctx:SpeakQlParser.DefaultValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#currentTimestamp.
    def visitCurrentTimestamp(self, ctx:SpeakQlParser.CurrentTimestampContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#expressionOrDefault.
    def visitExpressionOrDefault(self, ctx:SpeakQlParser.ExpressionOrDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#ifExists.
    def visitIfExists(self, ctx:SpeakQlParser.IfExistsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#ifNotExists.
    def visitIfNotExists(self, ctx:SpeakQlParser.IfNotExistsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#specificFunctionCall.
    def visitSpecificFunctionCall(self, ctx:SpeakQlParser.SpecificFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#aggregateFunctionCall.
    def visitAggregateFunctionCall(self, ctx:SpeakQlParser.AggregateFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#nonAggregateFunctionCall.
    def visitNonAggregateFunctionCall(self, ctx:SpeakQlParser.NonAggregateFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#scalarFunctionCall.
    def visitScalarFunctionCall(self, ctx:SpeakQlParser.ScalarFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#udfFunctionCall.
    def visitUdfFunctionCall(self, ctx:SpeakQlParser.UdfFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#passwordFunctionCall.
    def visitPasswordFunctionCall(self, ctx:SpeakQlParser.PasswordFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#leftParen.
    def visitLeftParen(self, ctx:SpeakQlParser.LeftParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#rightParen.
    def visitRightParen(self, ctx:SpeakQlParser.RightParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#simpleFunctionCall.
    def visitSimpleFunctionCall(self, ctx:SpeakQlParser.SimpleFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#dataTypeFunctionCall.
    def visitDataTypeFunctionCall(self, ctx:SpeakQlParser.DataTypeFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#valuesFunctionCall.
    def visitValuesFunctionCall(self, ctx:SpeakQlParser.ValuesFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#caseExpressionFunctionCall.
    def visitCaseExpressionFunctionCall(self, ctx:SpeakQlParser.CaseExpressionFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#caseFunctionCall.
    def visitCaseFunctionCall(self, ctx:SpeakQlParser.CaseFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#charFunctionCall.
    def visitCharFunctionCall(self, ctx:SpeakQlParser.CharFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#positionFunctionCall.
    def visitPositionFunctionCall(self, ctx:SpeakQlParser.PositionFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#substrFunctionCall.
    def visitSubstrFunctionCall(self, ctx:SpeakQlParser.SubstrFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#trimFunctionCall.
    def visitTrimFunctionCall(self, ctx:SpeakQlParser.TrimFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#weightFunctionCall.
    def visitWeightFunctionCall(self, ctx:SpeakQlParser.WeightFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#extractFunctionCall.
    def visitExtractFunctionCall(self, ctx:SpeakQlParser.ExtractFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#getFormatFunctionCall.
    def visitGetFormatFunctionCall(self, ctx:SpeakQlParser.GetFormatFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#jsonValueFunctionCall.
    def visitJsonValueFunctionCall(self, ctx:SpeakQlParser.JsonValueFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#caseFuncAlternative.
    def visitCaseFuncAlternative(self, ctx:SpeakQlParser.CaseFuncAlternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#levelWeightList.
    def visitLevelWeightList(self, ctx:SpeakQlParser.LevelWeightListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#levelWeightRange.
    def visitLevelWeightRange(self, ctx:SpeakQlParser.LevelWeightRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#levelInWeightListElement.
    def visitLevelInWeightListElement(self, ctx:SpeakQlParser.LevelInWeightListElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#aggregateWindowedFunction.
    def visitAggregateWindowedFunction(self, ctx:SpeakQlParser.AggregateWindowedFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#nonAggregateWindowedFunction.
    def visitNonAggregateWindowedFunction(self, ctx:SpeakQlParser.NonAggregateWindowedFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#overClause.
    def visitOverClause(self, ctx:SpeakQlParser.OverClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#windowSpec.
    def visitWindowSpec(self, ctx:SpeakQlParser.WindowSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#windowName.
    def visitWindowName(self, ctx:SpeakQlParser.WindowNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#frameClause.
    def visitFrameClause(self, ctx:SpeakQlParser.FrameClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#frameUnits.
    def visitFrameUnits(self, ctx:SpeakQlParser.FrameUnitsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#frameExtent.
    def visitFrameExtent(self, ctx:SpeakQlParser.FrameExtentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#frameBetween.
    def visitFrameBetween(self, ctx:SpeakQlParser.FrameBetweenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#frameRange.
    def visitFrameRange(self, ctx:SpeakQlParser.FrameRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#partitionClause.
    def visitPartitionClause(self, ctx:SpeakQlParser.PartitionClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#scalarFunctionName.
    def visitScalarFunctionName(self, ctx:SpeakQlParser.ScalarFunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#passwordFunctionClause.
    def visitPasswordFunctionClause(self, ctx:SpeakQlParser.PasswordFunctionClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#functionArgs.
    def visitFunctionArgs(self, ctx:SpeakQlParser.FunctionArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#functionArg.
    def visitFunctionArg(self, ctx:SpeakQlParser.FunctionArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#isExpression.
    def visitIsExpression(self, ctx:SpeakQlParser.IsExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#notExpression.
    def visitNotExpression(self, ctx:SpeakQlParser.NotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#logicalExpression.
    def visitLogicalExpression(self, ctx:SpeakQlParser.LogicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#predicateExpression.
    def visitPredicateExpression(self, ctx:SpeakQlParser.PredicateExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#soundsLikePredicate.
    def visitSoundsLikePredicate(self, ctx:SpeakQlParser.SoundsLikePredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#expressionAtomPredicate.
    def visitExpressionAtomPredicate(self, ctx:SpeakQlParser.ExpressionAtomPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#subqueryComparisonPredicate.
    def visitSubqueryComparisonPredicate(self, ctx:SpeakQlParser.SubqueryComparisonPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#jsonMemberOfPredicate.
    def visitJsonMemberOfPredicate(self, ctx:SpeakQlParser.JsonMemberOfPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#binaryComparisonPredicate.
    def visitBinaryComparisonPredicate(self, ctx:SpeakQlParser.BinaryComparisonPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#inPredicate.
    def visitInPredicate(self, ctx:SpeakQlParser.InPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#betweenPredicate.
    def visitBetweenPredicate(self, ctx:SpeakQlParser.BetweenPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#isNullPredicate.
    def visitIsNullPredicate(self, ctx:SpeakQlParser.IsNullPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#likePredicate.
    def visitLikePredicate(self, ctx:SpeakQlParser.LikePredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#regexpPredicate.
    def visitRegexpPredicate(self, ctx:SpeakQlParser.RegexpPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#unaryExpressionAtom.
    def visitUnaryExpressionAtom(self, ctx:SpeakQlParser.UnaryExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#collateExpressionAtom.
    def visitCollateExpressionAtom(self, ctx:SpeakQlParser.CollateExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#mysqlVariableExpressionAtom.
    def visitMysqlVariableExpressionAtom(self, ctx:SpeakQlParser.MysqlVariableExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#nestedExpressionAtom.
    def visitNestedExpressionAtom(self, ctx:SpeakQlParser.NestedExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#nestedRowExpressionAtom.
    def visitNestedRowExpressionAtom(self, ctx:SpeakQlParser.NestedRowExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#mathExpressionAtom.
    def visitMathExpressionAtom(self, ctx:SpeakQlParser.MathExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#existsExpressionAtom.
    def visitExistsExpressionAtom(self, ctx:SpeakQlParser.ExistsExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#intervalExpressionAtom.
    def visitIntervalExpressionAtom(self, ctx:SpeakQlParser.IntervalExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#jsonExpressionAtom.
    def visitJsonExpressionAtom(self, ctx:SpeakQlParser.JsonExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#subqueryExpressionAtom.
    def visitSubqueryExpressionAtom(self, ctx:SpeakQlParser.SubqueryExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#constantExpressionAtom.
    def visitConstantExpressionAtom(self, ctx:SpeakQlParser.ConstantExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#functionCallExpressionAtom.
    def visitFunctionCallExpressionAtom(self, ctx:SpeakQlParser.FunctionCallExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#binaryExpressionAtom.
    def visitBinaryExpressionAtom(self, ctx:SpeakQlParser.BinaryExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#fullColumnNameExpressionAtom.
    def visitFullColumnNameExpressionAtom(self, ctx:SpeakQlParser.FullColumnNameExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#bitExpressionAtom.
    def visitBitExpressionAtom(self, ctx:SpeakQlParser.BitExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#unaryOperator.
    def visitUnaryOperator(self, ctx:SpeakQlParser.UnaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#comparisonOperator.
    def visitComparisonOperator(self, ctx:SpeakQlParser.ComparisonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#logicalOperator.
    def visitLogicalOperator(self, ctx:SpeakQlParser.LogicalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#bitOperator.
    def visitBitOperator(self, ctx:SpeakQlParser.BitOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#mathOperator.
    def visitMathOperator(self, ctx:SpeakQlParser.MathOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#jsonOperator.
    def visitJsonOperator(self, ctx:SpeakQlParser.JsonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#charsetNameBase.
    def visitCharsetNameBase(self, ctx:SpeakQlParser.CharsetNameBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#transactionLevelBase.
    def visitTransactionLevelBase(self, ctx:SpeakQlParser.TransactionLevelBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#privilegesBase.
    def visitPrivilegesBase(self, ctx:SpeakQlParser.PrivilegesBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#intervalTypeBase.
    def visitIntervalTypeBase(self, ctx:SpeakQlParser.IntervalTypeBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#dataTypeBase.
    def visitDataTypeBase(self, ctx:SpeakQlParser.DataTypeBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#keywordsCanBeId.
    def visitKeywordsCanBeId(self, ctx:SpeakQlParser.KeywordsCanBeIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpeakQlParser#functionNameBase.
    def visitFunctionNameBase(self, ctx:SpeakQlParser.FunctionNameBaseContext):
        return self.visitChildren(ctx)



del SpeakQlParser
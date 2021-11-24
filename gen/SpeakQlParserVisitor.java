// Generated from C:/antlr_projects/speakql2\SpeakQlParser.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link SpeakQlParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface SpeakQlParserVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#root}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRoot(SpeakQlParser.RootContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#sqlStatements}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSqlStatements(SpeakQlParser.SqlStatementsContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#sqlStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSqlStatement(SpeakQlParser.SqlStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#emptyStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEmptyStatement(SpeakQlParser.EmptyStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#ddlStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDdlStatement(SpeakQlParser.DdlStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#dmlStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDmlStatement(SpeakQlParser.DmlStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#transactionStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTransactionStatement(SpeakQlParser.TransactionStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#replicationStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReplicationStatement(SpeakQlParser.ReplicationStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#preparedStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPreparedStatement(SpeakQlParser.PreparedStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#compoundStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCompoundStatement(SpeakQlParser.CompoundStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#administrationStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAdministrationStatement(SpeakQlParser.AdministrationStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#utilityStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUtilityStatement(SpeakQlParser.UtilityStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#createDatabase}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCreateDatabase(SpeakQlParser.CreateDatabaseContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#createEvent}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCreateEvent(SpeakQlParser.CreateEventContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#createIndex}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCreateIndex(SpeakQlParser.CreateIndexContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#createLogfileGroup}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCreateLogfileGroup(SpeakQlParser.CreateLogfileGroupContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#createProcedure}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCreateProcedure(SpeakQlParser.CreateProcedureContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#createFunction}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCreateFunction(SpeakQlParser.CreateFunctionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#createServer}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCreateServer(SpeakQlParser.CreateServerContext ctx);
	/**
	 * Visit a parse tree produced by the {@code copyCreateTable}
	 * labeled alternative in {@link SpeakQlParser#createTable}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCopyCreateTable(SpeakQlParser.CopyCreateTableContext ctx);
	/**
	 * Visit a parse tree produced by the {@code queryCreateTable}
	 * labeled alternative in {@link SpeakQlParser#createTable}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitQueryCreateTable(SpeakQlParser.QueryCreateTableContext ctx);
	/**
	 * Visit a parse tree produced by the {@code columnCreateTable}
	 * labeled alternative in {@link SpeakQlParser#createTable}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitColumnCreateTable(SpeakQlParser.ColumnCreateTableContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#createTablespaceInnodb}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCreateTablespaceInnodb(SpeakQlParser.CreateTablespaceInnodbContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#createTablespaceNdb}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCreateTablespaceNdb(SpeakQlParser.CreateTablespaceNdbContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#createTrigger}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCreateTrigger(SpeakQlParser.CreateTriggerContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#createView}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCreateView(SpeakQlParser.CreateViewContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#createDatabaseOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCreateDatabaseOption(SpeakQlParser.CreateDatabaseOptionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#ownerStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOwnerStatement(SpeakQlParser.OwnerStatementContext ctx);
	/**
	 * Visit a parse tree produced by the {@code preciseSchedule}
	 * labeled alternative in {@link SpeakQlParser#scheduleExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPreciseSchedule(SpeakQlParser.PreciseScheduleContext ctx);
	/**
	 * Visit a parse tree produced by the {@code intervalSchedule}
	 * labeled alternative in {@link SpeakQlParser#scheduleExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIntervalSchedule(SpeakQlParser.IntervalScheduleContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#timestampValue}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTimestampValue(SpeakQlParser.TimestampValueContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#intervalExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIntervalExpr(SpeakQlParser.IntervalExprContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#intervalType}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIntervalType(SpeakQlParser.IntervalTypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#enableType}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEnableType(SpeakQlParser.EnableTypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#indexType}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIndexType(SpeakQlParser.IndexTypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#indexOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIndexOption(SpeakQlParser.IndexOptionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#procedureParameter}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProcedureParameter(SpeakQlParser.ProcedureParameterContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#functionParameter}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunctionParameter(SpeakQlParser.FunctionParameterContext ctx);
	/**
	 * Visit a parse tree produced by the {@code routineComment}
	 * labeled alternative in {@link SpeakQlParser#routineOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRoutineComment(SpeakQlParser.RoutineCommentContext ctx);
	/**
	 * Visit a parse tree produced by the {@code routineLanguage}
	 * labeled alternative in {@link SpeakQlParser#routineOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRoutineLanguage(SpeakQlParser.RoutineLanguageContext ctx);
	/**
	 * Visit a parse tree produced by the {@code routineBehavior}
	 * labeled alternative in {@link SpeakQlParser#routineOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRoutineBehavior(SpeakQlParser.RoutineBehaviorContext ctx);
	/**
	 * Visit a parse tree produced by the {@code routineData}
	 * labeled alternative in {@link SpeakQlParser#routineOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRoutineData(SpeakQlParser.RoutineDataContext ctx);
	/**
	 * Visit a parse tree produced by the {@code routineSecurity}
	 * labeled alternative in {@link SpeakQlParser#routineOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRoutineSecurity(SpeakQlParser.RoutineSecurityContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#serverOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitServerOption(SpeakQlParser.ServerOptionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#createDefinitions}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCreateDefinitions(SpeakQlParser.CreateDefinitionsContext ctx);
	/**
	 * Visit a parse tree produced by the {@code columnDeclaration}
	 * labeled alternative in {@link SpeakQlParser#createDefinition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitColumnDeclaration(SpeakQlParser.ColumnDeclarationContext ctx);
	/**
	 * Visit a parse tree produced by the {@code constraintDeclaration}
	 * labeled alternative in {@link SpeakQlParser#createDefinition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitConstraintDeclaration(SpeakQlParser.ConstraintDeclarationContext ctx);
	/**
	 * Visit a parse tree produced by the {@code indexDeclaration}
	 * labeled alternative in {@link SpeakQlParser#createDefinition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIndexDeclaration(SpeakQlParser.IndexDeclarationContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#columnDefinition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitColumnDefinition(SpeakQlParser.ColumnDefinitionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code nullColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNullColumnConstraint(SpeakQlParser.NullColumnConstraintContext ctx);
	/**
	 * Visit a parse tree produced by the {@code defaultColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDefaultColumnConstraint(SpeakQlParser.DefaultColumnConstraintContext ctx);
	/**
	 * Visit a parse tree produced by the {@code visibilityColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVisibilityColumnConstraint(SpeakQlParser.VisibilityColumnConstraintContext ctx);
	/**
	 * Visit a parse tree produced by the {@code autoIncrementColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAutoIncrementColumnConstraint(SpeakQlParser.AutoIncrementColumnConstraintContext ctx);
	/**
	 * Visit a parse tree produced by the {@code primaryKeyColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrimaryKeyColumnConstraint(SpeakQlParser.PrimaryKeyColumnConstraintContext ctx);
	/**
	 * Visit a parse tree produced by the {@code uniqueKeyColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUniqueKeyColumnConstraint(SpeakQlParser.UniqueKeyColumnConstraintContext ctx);
	/**
	 * Visit a parse tree produced by the {@code commentColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCommentColumnConstraint(SpeakQlParser.CommentColumnConstraintContext ctx);
	/**
	 * Visit a parse tree produced by the {@code formatColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFormatColumnConstraint(SpeakQlParser.FormatColumnConstraintContext ctx);
	/**
	 * Visit a parse tree produced by the {@code storageColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStorageColumnConstraint(SpeakQlParser.StorageColumnConstraintContext ctx);
	/**
	 * Visit a parse tree produced by the {@code referenceColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReferenceColumnConstraint(SpeakQlParser.ReferenceColumnConstraintContext ctx);
	/**
	 * Visit a parse tree produced by the {@code collateColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCollateColumnConstraint(SpeakQlParser.CollateColumnConstraintContext ctx);
	/**
	 * Visit a parse tree produced by the {@code generatedColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitGeneratedColumnConstraint(SpeakQlParser.GeneratedColumnConstraintContext ctx);
	/**
	 * Visit a parse tree produced by the {@code serialDefaultColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSerialDefaultColumnConstraint(SpeakQlParser.SerialDefaultColumnConstraintContext ctx);
	/**
	 * Visit a parse tree produced by the {@code checkColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCheckColumnConstraint(SpeakQlParser.CheckColumnConstraintContext ctx);
	/**
	 * Visit a parse tree produced by the {@code primaryKeyTableConstraint}
	 * labeled alternative in {@link SpeakQlParser#tableConstraint}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrimaryKeyTableConstraint(SpeakQlParser.PrimaryKeyTableConstraintContext ctx);
	/**
	 * Visit a parse tree produced by the {@code uniqueKeyTableConstraint}
	 * labeled alternative in {@link SpeakQlParser#tableConstraint}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUniqueKeyTableConstraint(SpeakQlParser.UniqueKeyTableConstraintContext ctx);
	/**
	 * Visit a parse tree produced by the {@code foreignKeyTableConstraint}
	 * labeled alternative in {@link SpeakQlParser#tableConstraint}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitForeignKeyTableConstraint(SpeakQlParser.ForeignKeyTableConstraintContext ctx);
	/**
	 * Visit a parse tree produced by the {@code checkTableConstraint}
	 * labeled alternative in {@link SpeakQlParser#tableConstraint}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCheckTableConstraint(SpeakQlParser.CheckTableConstraintContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#referenceDefinition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReferenceDefinition(SpeakQlParser.ReferenceDefinitionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#referenceAction}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReferenceAction(SpeakQlParser.ReferenceActionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#referenceControlType}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReferenceControlType(SpeakQlParser.ReferenceControlTypeContext ctx);
	/**
	 * Visit a parse tree produced by the {@code simpleIndexDeclaration}
	 * labeled alternative in {@link SpeakQlParser#indexColumnDefinition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSimpleIndexDeclaration(SpeakQlParser.SimpleIndexDeclarationContext ctx);
	/**
	 * Visit a parse tree produced by the {@code specialIndexDeclaration}
	 * labeled alternative in {@link SpeakQlParser#indexColumnDefinition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSpecialIndexDeclaration(SpeakQlParser.SpecialIndexDeclarationContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tableOptionEngine}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableOptionEngine(SpeakQlParser.TableOptionEngineContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tableOptionAutoIncrement}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableOptionAutoIncrement(SpeakQlParser.TableOptionAutoIncrementContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tableOptionAverage}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableOptionAverage(SpeakQlParser.TableOptionAverageContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tableOptionCharset}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableOptionCharset(SpeakQlParser.TableOptionCharsetContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tableOptionChecksum}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableOptionChecksum(SpeakQlParser.TableOptionChecksumContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tableOptionCollate}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableOptionCollate(SpeakQlParser.TableOptionCollateContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tableOptionComment}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableOptionComment(SpeakQlParser.TableOptionCommentContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tableOptionCompression}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableOptionCompression(SpeakQlParser.TableOptionCompressionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tableOptionConnection}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableOptionConnection(SpeakQlParser.TableOptionConnectionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tableOptionDataDirectory}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableOptionDataDirectory(SpeakQlParser.TableOptionDataDirectoryContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tableOptionDelay}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableOptionDelay(SpeakQlParser.TableOptionDelayContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tableOptionEncryption}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableOptionEncryption(SpeakQlParser.TableOptionEncryptionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tableOptionIndexDirectory}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableOptionIndexDirectory(SpeakQlParser.TableOptionIndexDirectoryContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tableOptionInsertMethod}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableOptionInsertMethod(SpeakQlParser.TableOptionInsertMethodContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tableOptionKeyBlockSize}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableOptionKeyBlockSize(SpeakQlParser.TableOptionKeyBlockSizeContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tableOptionMaxRows}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableOptionMaxRows(SpeakQlParser.TableOptionMaxRowsContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tableOptionMinRows}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableOptionMinRows(SpeakQlParser.TableOptionMinRowsContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tableOptionPackKeys}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableOptionPackKeys(SpeakQlParser.TableOptionPackKeysContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tableOptionPassword}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableOptionPassword(SpeakQlParser.TableOptionPasswordContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tableOptionRowFormat}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableOptionRowFormat(SpeakQlParser.TableOptionRowFormatContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tableOptionRecalculation}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableOptionRecalculation(SpeakQlParser.TableOptionRecalculationContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tableOptionPersistent}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableOptionPersistent(SpeakQlParser.TableOptionPersistentContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tableOptionSamplePage}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableOptionSamplePage(SpeakQlParser.TableOptionSamplePageContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tableOptionTablespace}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableOptionTablespace(SpeakQlParser.TableOptionTablespaceContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tableOptionTableType}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableOptionTableType(SpeakQlParser.TableOptionTableTypeContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tableOptionUnion}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableOptionUnion(SpeakQlParser.TableOptionUnionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#tableType}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableType(SpeakQlParser.TableTypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#tablespaceStorage}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTablespaceStorage(SpeakQlParser.TablespaceStorageContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#partitionDefinitions}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPartitionDefinitions(SpeakQlParser.PartitionDefinitionsContext ctx);
	/**
	 * Visit a parse tree produced by the {@code partitionFunctionHash}
	 * labeled alternative in {@link SpeakQlParser#partitionFunctionDefinition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPartitionFunctionHash(SpeakQlParser.PartitionFunctionHashContext ctx);
	/**
	 * Visit a parse tree produced by the {@code partitionFunctionKey}
	 * labeled alternative in {@link SpeakQlParser#partitionFunctionDefinition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPartitionFunctionKey(SpeakQlParser.PartitionFunctionKeyContext ctx);
	/**
	 * Visit a parse tree produced by the {@code partitionFunctionRange}
	 * labeled alternative in {@link SpeakQlParser#partitionFunctionDefinition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPartitionFunctionRange(SpeakQlParser.PartitionFunctionRangeContext ctx);
	/**
	 * Visit a parse tree produced by the {@code partitionFunctionList}
	 * labeled alternative in {@link SpeakQlParser#partitionFunctionDefinition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPartitionFunctionList(SpeakQlParser.PartitionFunctionListContext ctx);
	/**
	 * Visit a parse tree produced by the {@code subPartitionFunctionHash}
	 * labeled alternative in {@link SpeakQlParser#subpartitionFunctionDefinition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSubPartitionFunctionHash(SpeakQlParser.SubPartitionFunctionHashContext ctx);
	/**
	 * Visit a parse tree produced by the {@code subPartitionFunctionKey}
	 * labeled alternative in {@link SpeakQlParser#subpartitionFunctionDefinition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSubPartitionFunctionKey(SpeakQlParser.SubPartitionFunctionKeyContext ctx);
	/**
	 * Visit a parse tree produced by the {@code partitionComparison}
	 * labeled alternative in {@link SpeakQlParser#partitionDefinition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPartitionComparison(SpeakQlParser.PartitionComparisonContext ctx);
	/**
	 * Visit a parse tree produced by the {@code partitionListAtom}
	 * labeled alternative in {@link SpeakQlParser#partitionDefinition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPartitionListAtom(SpeakQlParser.PartitionListAtomContext ctx);
	/**
	 * Visit a parse tree produced by the {@code partitionListVector}
	 * labeled alternative in {@link SpeakQlParser#partitionDefinition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPartitionListVector(SpeakQlParser.PartitionListVectorContext ctx);
	/**
	 * Visit a parse tree produced by the {@code partitionSimple}
	 * labeled alternative in {@link SpeakQlParser#partitionDefinition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPartitionSimple(SpeakQlParser.PartitionSimpleContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#partitionDefinerAtom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPartitionDefinerAtom(SpeakQlParser.PartitionDefinerAtomContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#partitionDefinerVector}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPartitionDefinerVector(SpeakQlParser.PartitionDefinerVectorContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#subpartitionDefinition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSubpartitionDefinition(SpeakQlParser.SubpartitionDefinitionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code partitionOptionEngine}
	 * labeled alternative in {@link SpeakQlParser#partitionOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPartitionOptionEngine(SpeakQlParser.PartitionOptionEngineContext ctx);
	/**
	 * Visit a parse tree produced by the {@code partitionOptionComment}
	 * labeled alternative in {@link SpeakQlParser#partitionOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPartitionOptionComment(SpeakQlParser.PartitionOptionCommentContext ctx);
	/**
	 * Visit a parse tree produced by the {@code partitionOptionDataDirectory}
	 * labeled alternative in {@link SpeakQlParser#partitionOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPartitionOptionDataDirectory(SpeakQlParser.PartitionOptionDataDirectoryContext ctx);
	/**
	 * Visit a parse tree produced by the {@code partitionOptionIndexDirectory}
	 * labeled alternative in {@link SpeakQlParser#partitionOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPartitionOptionIndexDirectory(SpeakQlParser.PartitionOptionIndexDirectoryContext ctx);
	/**
	 * Visit a parse tree produced by the {@code partitionOptionMaxRows}
	 * labeled alternative in {@link SpeakQlParser#partitionOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPartitionOptionMaxRows(SpeakQlParser.PartitionOptionMaxRowsContext ctx);
	/**
	 * Visit a parse tree produced by the {@code partitionOptionMinRows}
	 * labeled alternative in {@link SpeakQlParser#partitionOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPartitionOptionMinRows(SpeakQlParser.PartitionOptionMinRowsContext ctx);
	/**
	 * Visit a parse tree produced by the {@code partitionOptionTablespace}
	 * labeled alternative in {@link SpeakQlParser#partitionOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPartitionOptionTablespace(SpeakQlParser.PartitionOptionTablespaceContext ctx);
	/**
	 * Visit a parse tree produced by the {@code partitionOptionNodeGroup}
	 * labeled alternative in {@link SpeakQlParser#partitionOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPartitionOptionNodeGroup(SpeakQlParser.PartitionOptionNodeGroupContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterSimpleDatabase}
	 * labeled alternative in {@link SpeakQlParser#alterDatabase}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterSimpleDatabase(SpeakQlParser.AlterSimpleDatabaseContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterUpgradeName}
	 * labeled alternative in {@link SpeakQlParser#alterDatabase}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterUpgradeName(SpeakQlParser.AlterUpgradeNameContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#alterEvent}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterEvent(SpeakQlParser.AlterEventContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#alterFunction}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterFunction(SpeakQlParser.AlterFunctionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#alterInstance}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterInstance(SpeakQlParser.AlterInstanceContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#alterLogfileGroup}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterLogfileGroup(SpeakQlParser.AlterLogfileGroupContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#alterProcedure}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterProcedure(SpeakQlParser.AlterProcedureContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#alterServer}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterServer(SpeakQlParser.AlterServerContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#alterTable}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterTable(SpeakQlParser.AlterTableContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#alterTablespace}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterTablespace(SpeakQlParser.AlterTablespaceContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#alterView}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterView(SpeakQlParser.AlterViewContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByTableOption}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByTableOption(SpeakQlParser.AlterByTableOptionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByAddColumn}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByAddColumn(SpeakQlParser.AlterByAddColumnContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByAddColumns}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByAddColumns(SpeakQlParser.AlterByAddColumnsContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByAddIndex}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByAddIndex(SpeakQlParser.AlterByAddIndexContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByAddPrimaryKey}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByAddPrimaryKey(SpeakQlParser.AlterByAddPrimaryKeyContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByAddUniqueKey}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByAddUniqueKey(SpeakQlParser.AlterByAddUniqueKeyContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByAddSpecialIndex}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByAddSpecialIndex(SpeakQlParser.AlterByAddSpecialIndexContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByAddForeignKey}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByAddForeignKey(SpeakQlParser.AlterByAddForeignKeyContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByAddCheckTableConstraint}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByAddCheckTableConstraint(SpeakQlParser.AlterByAddCheckTableConstraintContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterBySetAlgorithm}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterBySetAlgorithm(SpeakQlParser.AlterBySetAlgorithmContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByChangeDefault}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByChangeDefault(SpeakQlParser.AlterByChangeDefaultContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByChangeColumn}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByChangeColumn(SpeakQlParser.AlterByChangeColumnContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByRenameColumn}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByRenameColumn(SpeakQlParser.AlterByRenameColumnContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByLock}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByLock(SpeakQlParser.AlterByLockContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByModifyColumn}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByModifyColumn(SpeakQlParser.AlterByModifyColumnContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByDropColumn}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByDropColumn(SpeakQlParser.AlterByDropColumnContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByDropConstraintCheck}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByDropConstraintCheck(SpeakQlParser.AlterByDropConstraintCheckContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByDropPrimaryKey}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByDropPrimaryKey(SpeakQlParser.AlterByDropPrimaryKeyContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByRenameIndex}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByRenameIndex(SpeakQlParser.AlterByRenameIndexContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByAlterIndexVisibility}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByAlterIndexVisibility(SpeakQlParser.AlterByAlterIndexVisibilityContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByDropIndex}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByDropIndex(SpeakQlParser.AlterByDropIndexContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByDropForeignKey}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByDropForeignKey(SpeakQlParser.AlterByDropForeignKeyContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByDisableKeys}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByDisableKeys(SpeakQlParser.AlterByDisableKeysContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByEnableKeys}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByEnableKeys(SpeakQlParser.AlterByEnableKeysContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByRename}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByRename(SpeakQlParser.AlterByRenameContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByOrder}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByOrder(SpeakQlParser.AlterByOrderContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByConvertCharset}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByConvertCharset(SpeakQlParser.AlterByConvertCharsetContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByDefaultCharset}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByDefaultCharset(SpeakQlParser.AlterByDefaultCharsetContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByDiscardTablespace}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByDiscardTablespace(SpeakQlParser.AlterByDiscardTablespaceContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByImportTablespace}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByImportTablespace(SpeakQlParser.AlterByImportTablespaceContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByForce}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByForce(SpeakQlParser.AlterByForceContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByValidate}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByValidate(SpeakQlParser.AlterByValidateContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByAddPartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByAddPartition(SpeakQlParser.AlterByAddPartitionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByDropPartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByDropPartition(SpeakQlParser.AlterByDropPartitionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByDiscardPartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByDiscardPartition(SpeakQlParser.AlterByDiscardPartitionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByImportPartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByImportPartition(SpeakQlParser.AlterByImportPartitionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByTruncatePartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByTruncatePartition(SpeakQlParser.AlterByTruncatePartitionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByCoalescePartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByCoalescePartition(SpeakQlParser.AlterByCoalescePartitionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByReorganizePartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByReorganizePartition(SpeakQlParser.AlterByReorganizePartitionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByExchangePartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByExchangePartition(SpeakQlParser.AlterByExchangePartitionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByAnalyzePartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByAnalyzePartition(SpeakQlParser.AlterByAnalyzePartitionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByCheckPartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByCheckPartition(SpeakQlParser.AlterByCheckPartitionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByOptimizePartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByOptimizePartition(SpeakQlParser.AlterByOptimizePartitionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByRebuildPartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByRebuildPartition(SpeakQlParser.AlterByRebuildPartitionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByRepairPartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByRepairPartition(SpeakQlParser.AlterByRepairPartitionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByRemovePartitioning}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByRemovePartitioning(SpeakQlParser.AlterByRemovePartitioningContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterByUpgradePartitioning}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterByUpgradePartitioning(SpeakQlParser.AlterByUpgradePartitioningContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#dropDatabase}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDropDatabase(SpeakQlParser.DropDatabaseContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#dropEvent}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDropEvent(SpeakQlParser.DropEventContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#dropIndex}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDropIndex(SpeakQlParser.DropIndexContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#dropLogfileGroup}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDropLogfileGroup(SpeakQlParser.DropLogfileGroupContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#dropProcedure}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDropProcedure(SpeakQlParser.DropProcedureContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#dropFunction}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDropFunction(SpeakQlParser.DropFunctionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#dropServer}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDropServer(SpeakQlParser.DropServerContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#dropTable}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDropTable(SpeakQlParser.DropTableContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#dropTablespace}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDropTablespace(SpeakQlParser.DropTablespaceContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#dropTrigger}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDropTrigger(SpeakQlParser.DropTriggerContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#dropView}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDropView(SpeakQlParser.DropViewContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#renameTable}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRenameTable(SpeakQlParser.RenameTableContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#renameTableClause}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRenameTableClause(SpeakQlParser.RenameTableClauseContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#truncateTable}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTruncateTable(SpeakQlParser.TruncateTableContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#callStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCallStatement(SpeakQlParser.CallStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#deleteStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeleteStatement(SpeakQlParser.DeleteStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#doStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDoStatement(SpeakQlParser.DoStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#handlerStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitHandlerStatement(SpeakQlParser.HandlerStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#insertStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInsertStatement(SpeakQlParser.InsertStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#loadDataStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLoadDataStatement(SpeakQlParser.LoadDataStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#loadXmlStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLoadXmlStatement(SpeakQlParser.LoadXmlStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#replaceStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReplaceStatement(SpeakQlParser.ReplaceStatementContext ctx);
	/**
	 * Visit a parse tree produced by the {@code simpleSelect}
	 * labeled alternative in {@link SpeakQlParser#selectStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSimpleSelect(SpeakQlParser.SimpleSelectContext ctx);
	/**
	 * Visit a parse tree produced by the {@code parenthesisSelect}
	 * labeled alternative in {@link SpeakQlParser#selectStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParenthesisSelect(SpeakQlParser.ParenthesisSelectContext ctx);
	/**
	 * Visit a parse tree produced by the {@code unionSelect}
	 * labeled alternative in {@link SpeakQlParser#selectStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUnionSelect(SpeakQlParser.UnionSelectContext ctx);
	/**
	 * Visit a parse tree produced by the {@code unionParenthesisSelect}
	 * labeled alternative in {@link SpeakQlParser#selectStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUnionParenthesisSelect(SpeakQlParser.UnionParenthesisSelectContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#updateStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUpdateStatement(SpeakQlParser.UpdateStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#insertStatementValue}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInsertStatementValue(SpeakQlParser.InsertStatementValueContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#updatedElement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUpdatedElement(SpeakQlParser.UpdatedElementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#assignmentField}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssignmentField(SpeakQlParser.AssignmentFieldContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#lockClause}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLockClause(SpeakQlParser.LockClauseContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#singleDeleteStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSingleDeleteStatement(SpeakQlParser.SingleDeleteStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#multipleDeleteStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMultipleDeleteStatement(SpeakQlParser.MultipleDeleteStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#handlerOpenStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitHandlerOpenStatement(SpeakQlParser.HandlerOpenStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#handlerReadIndexStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitHandlerReadIndexStatement(SpeakQlParser.HandlerReadIndexStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#handlerReadStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitHandlerReadStatement(SpeakQlParser.HandlerReadStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#handlerCloseStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitHandlerCloseStatement(SpeakQlParser.HandlerCloseStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#singleUpdateStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSingleUpdateStatement(SpeakQlParser.SingleUpdateStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#multipleUpdateStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMultipleUpdateStatement(SpeakQlParser.MultipleUpdateStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#orderByClause}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOrderByClause(SpeakQlParser.OrderByClauseContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#orderByExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOrderByExpression(SpeakQlParser.OrderByExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#tableSources}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableSources(SpeakQlParser.TableSourcesContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tableSourceBase}
	 * labeled alternative in {@link SpeakQlParser#tableSource}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableSourceBase(SpeakQlParser.TableSourceBaseContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tableSourceNested}
	 * labeled alternative in {@link SpeakQlParser#tableSource}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableSourceNested(SpeakQlParser.TableSourceNestedContext ctx);
	/**
	 * Visit a parse tree produced by the {@code atomTableItem}
	 * labeled alternative in {@link SpeakQlParser#tableSourceItem}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAtomTableItem(SpeakQlParser.AtomTableItemContext ctx);
	/**
	 * Visit a parse tree produced by the {@code subqueryTableItem}
	 * labeled alternative in {@link SpeakQlParser#tableSourceItem}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSubqueryTableItem(SpeakQlParser.SubqueryTableItemContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tableSourcesItem}
	 * labeled alternative in {@link SpeakQlParser#tableSourceItem}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableSourcesItem(SpeakQlParser.TableSourcesItemContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#indexHint}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIndexHint(SpeakQlParser.IndexHintContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#indexHintType}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIndexHintType(SpeakQlParser.IndexHintTypeContext ctx);
	/**
	 * Visit a parse tree produced by the {@code innerJoin}
	 * labeled alternative in {@link SpeakQlParser#joinPart}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInnerJoin(SpeakQlParser.InnerJoinContext ctx);
	/**
	 * Visit a parse tree produced by the {@code straightJoin}
	 * labeled alternative in {@link SpeakQlParser#joinPart}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStraightJoin(SpeakQlParser.StraightJoinContext ctx);
	/**
	 * Visit a parse tree produced by the {@code outerJoin}
	 * labeled alternative in {@link SpeakQlParser#joinPart}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOuterJoin(SpeakQlParser.OuterJoinContext ctx);
	/**
	 * Visit a parse tree produced by the {@code naturalJoin}
	 * labeled alternative in {@link SpeakQlParser#joinPart}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNaturalJoin(SpeakQlParser.NaturalJoinContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#joinKeyword}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitJoinKeyword(SpeakQlParser.JoinKeywordContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#queryExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitQueryExpression(SpeakQlParser.QueryExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#queryExpressionNointo}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitQueryExpressionNointo(SpeakQlParser.QueryExpressionNointoContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#querySpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitQuerySpecification(SpeakQlParser.QuerySpecificationContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#selectModifierExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSelectModifierExpression(SpeakQlParser.SelectModifierExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#selectExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSelectExpression(SpeakQlParser.SelectExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#tableExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableExpression(SpeakQlParser.TableExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#selectClause}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSelectClause(SpeakQlParser.SelectClauseContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#selectKeyword}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSelectKeyword(SpeakQlParser.SelectKeywordContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#querySpecificationNointo}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitQuerySpecificationNointo(SpeakQlParser.QuerySpecificationNointoContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#unionParenthesis}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUnionParenthesis(SpeakQlParser.UnionParenthesisContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#unionStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUnionStatement(SpeakQlParser.UnionStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#selectSpec}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSelectSpec(SpeakQlParser.SelectSpecContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#selectElements}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSelectElements(SpeakQlParser.SelectElementsContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#selectElementDelimiter}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSelectElementDelimiter(SpeakQlParser.SelectElementDelimiterContext ctx);
	/**
	 * Visit a parse tree produced by the {@code selectStarElement}
	 * labeled alternative in {@link SpeakQlParser#selectElement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSelectStarElement(SpeakQlParser.SelectStarElementContext ctx);
	/**
	 * Visit a parse tree produced by the {@code selectColumnElement}
	 * labeled alternative in {@link SpeakQlParser#selectElement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSelectColumnElement(SpeakQlParser.SelectColumnElementContext ctx);
	/**
	 * Visit a parse tree produced by the {@code selectFunctionElement}
	 * labeled alternative in {@link SpeakQlParser#selectElement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSelectFunctionElement(SpeakQlParser.SelectFunctionElementContext ctx);
	/**
	 * Visit a parse tree produced by the {@code selectExpressionElement}
	 * labeled alternative in {@link SpeakQlParser#selectElement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSelectExpressionElement(SpeakQlParser.SelectExpressionElementContext ctx);
	/**
	 * Visit a parse tree produced by the {@code selectIntoVariables}
	 * labeled alternative in {@link SpeakQlParser#selectIntoExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSelectIntoVariables(SpeakQlParser.SelectIntoVariablesContext ctx);
	/**
	 * Visit a parse tree produced by the {@code selectIntoDumpFile}
	 * labeled alternative in {@link SpeakQlParser#selectIntoExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSelectIntoDumpFile(SpeakQlParser.SelectIntoDumpFileContext ctx);
	/**
	 * Visit a parse tree produced by the {@code selectIntoTextFile}
	 * labeled alternative in {@link SpeakQlParser#selectIntoExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSelectIntoTextFile(SpeakQlParser.SelectIntoTextFileContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#selectFieldsInto}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSelectFieldsInto(SpeakQlParser.SelectFieldsIntoContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#selectLinesInto}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSelectLinesInto(SpeakQlParser.SelectLinesIntoContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#fromClause}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFromClause(SpeakQlParser.FromClauseContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#fromKeyword}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFromKeyword(SpeakQlParser.FromKeywordContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#groupByClause}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitGroupByClause(SpeakQlParser.GroupByClauseContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#havingClause}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitHavingClause(SpeakQlParser.HavingClauseContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#windowClause}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWindowClause(SpeakQlParser.WindowClauseContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#groupByItem}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitGroupByItem(SpeakQlParser.GroupByItemContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#limitClause}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLimitClause(SpeakQlParser.LimitClauseContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#limitClauseAtom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLimitClauseAtom(SpeakQlParser.LimitClauseAtomContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#startTransaction}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStartTransaction(SpeakQlParser.StartTransactionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#beginWork}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBeginWork(SpeakQlParser.BeginWorkContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#commitWork}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCommitWork(SpeakQlParser.CommitWorkContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#rollbackWork}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRollbackWork(SpeakQlParser.RollbackWorkContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#savepointStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSavepointStatement(SpeakQlParser.SavepointStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#rollbackStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRollbackStatement(SpeakQlParser.RollbackStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#releaseStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReleaseStatement(SpeakQlParser.ReleaseStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#lockTables}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLockTables(SpeakQlParser.LockTablesContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#unlockTables}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUnlockTables(SpeakQlParser.UnlockTablesContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#setAutocommitStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSetAutocommitStatement(SpeakQlParser.SetAutocommitStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#setTransactionStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSetTransactionStatement(SpeakQlParser.SetTransactionStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#transactionMode}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTransactionMode(SpeakQlParser.TransactionModeContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#lockTableElement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLockTableElement(SpeakQlParser.LockTableElementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#lockAction}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLockAction(SpeakQlParser.LockActionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#transactionOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTransactionOption(SpeakQlParser.TransactionOptionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#transactionLevel}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTransactionLevel(SpeakQlParser.TransactionLevelContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#changeMaster}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitChangeMaster(SpeakQlParser.ChangeMasterContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#changeReplicationFilter}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitChangeReplicationFilter(SpeakQlParser.ChangeReplicationFilterContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#purgeBinaryLogs}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPurgeBinaryLogs(SpeakQlParser.PurgeBinaryLogsContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#resetMaster}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitResetMaster(SpeakQlParser.ResetMasterContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#resetSlave}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitResetSlave(SpeakQlParser.ResetSlaveContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#startSlave}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStartSlave(SpeakQlParser.StartSlaveContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#stopSlave}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStopSlave(SpeakQlParser.StopSlaveContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#startGroupReplication}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStartGroupReplication(SpeakQlParser.StartGroupReplicationContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#stopGroupReplication}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStopGroupReplication(SpeakQlParser.StopGroupReplicationContext ctx);
	/**
	 * Visit a parse tree produced by the {@code masterStringOption}
	 * labeled alternative in {@link SpeakQlParser#masterOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMasterStringOption(SpeakQlParser.MasterStringOptionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code masterDecimalOption}
	 * labeled alternative in {@link SpeakQlParser#masterOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMasterDecimalOption(SpeakQlParser.MasterDecimalOptionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code masterBoolOption}
	 * labeled alternative in {@link SpeakQlParser#masterOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMasterBoolOption(SpeakQlParser.MasterBoolOptionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code masterRealOption}
	 * labeled alternative in {@link SpeakQlParser#masterOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMasterRealOption(SpeakQlParser.MasterRealOptionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code masterUidListOption}
	 * labeled alternative in {@link SpeakQlParser#masterOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMasterUidListOption(SpeakQlParser.MasterUidListOptionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#stringMasterOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStringMasterOption(SpeakQlParser.StringMasterOptionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#decimalMasterOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDecimalMasterOption(SpeakQlParser.DecimalMasterOptionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#boolMasterOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBoolMasterOption(SpeakQlParser.BoolMasterOptionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#channelOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitChannelOption(SpeakQlParser.ChannelOptionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code doDbReplication}
	 * labeled alternative in {@link SpeakQlParser#replicationFilter}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDoDbReplication(SpeakQlParser.DoDbReplicationContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ignoreDbReplication}
	 * labeled alternative in {@link SpeakQlParser#replicationFilter}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIgnoreDbReplication(SpeakQlParser.IgnoreDbReplicationContext ctx);
	/**
	 * Visit a parse tree produced by the {@code doTableReplication}
	 * labeled alternative in {@link SpeakQlParser#replicationFilter}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDoTableReplication(SpeakQlParser.DoTableReplicationContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ignoreTableReplication}
	 * labeled alternative in {@link SpeakQlParser#replicationFilter}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIgnoreTableReplication(SpeakQlParser.IgnoreTableReplicationContext ctx);
	/**
	 * Visit a parse tree produced by the {@code wildDoTableReplication}
	 * labeled alternative in {@link SpeakQlParser#replicationFilter}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWildDoTableReplication(SpeakQlParser.WildDoTableReplicationContext ctx);
	/**
	 * Visit a parse tree produced by the {@code wildIgnoreTableReplication}
	 * labeled alternative in {@link SpeakQlParser#replicationFilter}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWildIgnoreTableReplication(SpeakQlParser.WildIgnoreTableReplicationContext ctx);
	/**
	 * Visit a parse tree produced by the {@code rewriteDbReplication}
	 * labeled alternative in {@link SpeakQlParser#replicationFilter}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRewriteDbReplication(SpeakQlParser.RewriteDbReplicationContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#tablePair}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTablePair(SpeakQlParser.TablePairContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#threadType}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitThreadType(SpeakQlParser.ThreadTypeContext ctx);
	/**
	 * Visit a parse tree produced by the {@code gtidsUntilOption}
	 * labeled alternative in {@link SpeakQlParser#untilOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitGtidsUntilOption(SpeakQlParser.GtidsUntilOptionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code masterLogUntilOption}
	 * labeled alternative in {@link SpeakQlParser#untilOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMasterLogUntilOption(SpeakQlParser.MasterLogUntilOptionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code relayLogUntilOption}
	 * labeled alternative in {@link SpeakQlParser#untilOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRelayLogUntilOption(SpeakQlParser.RelayLogUntilOptionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code sqlGapsUntilOption}
	 * labeled alternative in {@link SpeakQlParser#untilOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSqlGapsUntilOption(SpeakQlParser.SqlGapsUntilOptionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code userConnectionOption}
	 * labeled alternative in {@link SpeakQlParser#connectionOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUserConnectionOption(SpeakQlParser.UserConnectionOptionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code passwordConnectionOption}
	 * labeled alternative in {@link SpeakQlParser#connectionOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPasswordConnectionOption(SpeakQlParser.PasswordConnectionOptionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code defaultAuthConnectionOption}
	 * labeled alternative in {@link SpeakQlParser#connectionOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDefaultAuthConnectionOption(SpeakQlParser.DefaultAuthConnectionOptionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code pluginDirConnectionOption}
	 * labeled alternative in {@link SpeakQlParser#connectionOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPluginDirConnectionOption(SpeakQlParser.PluginDirConnectionOptionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#gtuidSet}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitGtuidSet(SpeakQlParser.GtuidSetContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#xaStartTransaction}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitXaStartTransaction(SpeakQlParser.XaStartTransactionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#xaEndTransaction}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitXaEndTransaction(SpeakQlParser.XaEndTransactionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#xaPrepareStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitXaPrepareStatement(SpeakQlParser.XaPrepareStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#xaCommitWork}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitXaCommitWork(SpeakQlParser.XaCommitWorkContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#xaRollbackWork}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitXaRollbackWork(SpeakQlParser.XaRollbackWorkContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#xaRecoverWork}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitXaRecoverWork(SpeakQlParser.XaRecoverWorkContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#prepareStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrepareStatement(SpeakQlParser.PrepareStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#executeStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExecuteStatement(SpeakQlParser.ExecuteStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#deallocatePrepare}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeallocatePrepare(SpeakQlParser.DeallocatePrepareContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#routineBody}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRoutineBody(SpeakQlParser.RoutineBodyContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#blockStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBlockStatement(SpeakQlParser.BlockStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#caseStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCaseStatement(SpeakQlParser.CaseStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#ifStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIfStatement(SpeakQlParser.IfStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#iterateStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIterateStatement(SpeakQlParser.IterateStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#leaveStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLeaveStatement(SpeakQlParser.LeaveStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#loopStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLoopStatement(SpeakQlParser.LoopStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#repeatStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRepeatStatement(SpeakQlParser.RepeatStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#returnStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReturnStatement(SpeakQlParser.ReturnStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#whileStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWhileStatement(SpeakQlParser.WhileStatementContext ctx);
	/**
	 * Visit a parse tree produced by the {@code CloseCursor}
	 * labeled alternative in {@link SpeakQlParser#cursorStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCloseCursor(SpeakQlParser.CloseCursorContext ctx);
	/**
	 * Visit a parse tree produced by the {@code FetchCursor}
	 * labeled alternative in {@link SpeakQlParser#cursorStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFetchCursor(SpeakQlParser.FetchCursorContext ctx);
	/**
	 * Visit a parse tree produced by the {@code OpenCursor}
	 * labeled alternative in {@link SpeakQlParser#cursorStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOpenCursor(SpeakQlParser.OpenCursorContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#declareVariable}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeclareVariable(SpeakQlParser.DeclareVariableContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#declareCondition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeclareCondition(SpeakQlParser.DeclareConditionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#declareCursor}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeclareCursor(SpeakQlParser.DeclareCursorContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#declareHandler}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeclareHandler(SpeakQlParser.DeclareHandlerContext ctx);
	/**
	 * Visit a parse tree produced by the {@code handlerConditionCode}
	 * labeled alternative in {@link SpeakQlParser#handlerConditionValue}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitHandlerConditionCode(SpeakQlParser.HandlerConditionCodeContext ctx);
	/**
	 * Visit a parse tree produced by the {@code handlerConditionState}
	 * labeled alternative in {@link SpeakQlParser#handlerConditionValue}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitHandlerConditionState(SpeakQlParser.HandlerConditionStateContext ctx);
	/**
	 * Visit a parse tree produced by the {@code handlerConditionName}
	 * labeled alternative in {@link SpeakQlParser#handlerConditionValue}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitHandlerConditionName(SpeakQlParser.HandlerConditionNameContext ctx);
	/**
	 * Visit a parse tree produced by the {@code handlerConditionWarning}
	 * labeled alternative in {@link SpeakQlParser#handlerConditionValue}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitHandlerConditionWarning(SpeakQlParser.HandlerConditionWarningContext ctx);
	/**
	 * Visit a parse tree produced by the {@code handlerConditionNotfound}
	 * labeled alternative in {@link SpeakQlParser#handlerConditionValue}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitHandlerConditionNotfound(SpeakQlParser.HandlerConditionNotfoundContext ctx);
	/**
	 * Visit a parse tree produced by the {@code handlerConditionException}
	 * labeled alternative in {@link SpeakQlParser#handlerConditionValue}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitHandlerConditionException(SpeakQlParser.HandlerConditionExceptionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#procedureSqlStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProcedureSqlStatement(SpeakQlParser.ProcedureSqlStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#caseAlternative}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCaseAlternative(SpeakQlParser.CaseAlternativeContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#elifAlternative}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitElifAlternative(SpeakQlParser.ElifAlternativeContext ctx);
	/**
	 * Visit a parse tree produced by the {@code alterUserMysqlV56}
	 * labeled alternative in {@link SpeakQlParser#alterUser}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterUserMysqlV56(SpeakQlParser.AlterUserMysqlV56Context ctx);
	/**
	 * Visit a parse tree produced by the {@code alterUserMysqlV57}
	 * labeled alternative in {@link SpeakQlParser#alterUser}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlterUserMysqlV57(SpeakQlParser.AlterUserMysqlV57Context ctx);
	/**
	 * Visit a parse tree produced by the {@code createUserMysqlV56}
	 * labeled alternative in {@link SpeakQlParser#createUser}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCreateUserMysqlV56(SpeakQlParser.CreateUserMysqlV56Context ctx);
	/**
	 * Visit a parse tree produced by the {@code createUserMysqlV57}
	 * labeled alternative in {@link SpeakQlParser#createUser}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCreateUserMysqlV57(SpeakQlParser.CreateUserMysqlV57Context ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#dropUser}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDropUser(SpeakQlParser.DropUserContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#grantStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitGrantStatement(SpeakQlParser.GrantStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#roleOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRoleOption(SpeakQlParser.RoleOptionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#grantProxy}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitGrantProxy(SpeakQlParser.GrantProxyContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#renameUser}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRenameUser(SpeakQlParser.RenameUserContext ctx);
	/**
	 * Visit a parse tree produced by the {@code detailRevoke}
	 * labeled alternative in {@link SpeakQlParser#revokeStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDetailRevoke(SpeakQlParser.DetailRevokeContext ctx);
	/**
	 * Visit a parse tree produced by the {@code shortRevoke}
	 * labeled alternative in {@link SpeakQlParser#revokeStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitShortRevoke(SpeakQlParser.ShortRevokeContext ctx);
	/**
	 * Visit a parse tree produced by the {@code roleRevoke}
	 * labeled alternative in {@link SpeakQlParser#revokeStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRoleRevoke(SpeakQlParser.RoleRevokeContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#revokeProxy}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRevokeProxy(SpeakQlParser.RevokeProxyContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#setPasswordStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSetPasswordStatement(SpeakQlParser.SetPasswordStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#userSpecification}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUserSpecification(SpeakQlParser.UserSpecificationContext ctx);
	/**
	 * Visit a parse tree produced by the {@code passwordAuthOption}
	 * labeled alternative in {@link SpeakQlParser#userAuthOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPasswordAuthOption(SpeakQlParser.PasswordAuthOptionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code stringAuthOption}
	 * labeled alternative in {@link SpeakQlParser#userAuthOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStringAuthOption(SpeakQlParser.StringAuthOptionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code hashAuthOption}
	 * labeled alternative in {@link SpeakQlParser#userAuthOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitHashAuthOption(SpeakQlParser.HashAuthOptionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code simpleAuthOption}
	 * labeled alternative in {@link SpeakQlParser#userAuthOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSimpleAuthOption(SpeakQlParser.SimpleAuthOptionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#tlsOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTlsOption(SpeakQlParser.TlsOptionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#userResourceOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUserResourceOption(SpeakQlParser.UserResourceOptionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#userPasswordOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUserPasswordOption(SpeakQlParser.UserPasswordOptionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#userLockOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUserLockOption(SpeakQlParser.UserLockOptionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#privelegeClause}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrivelegeClause(SpeakQlParser.PrivelegeClauseContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#privilege}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrivilege(SpeakQlParser.PrivilegeContext ctx);
	/**
	 * Visit a parse tree produced by the {@code currentSchemaPriviLevel}
	 * labeled alternative in {@link SpeakQlParser#privilegeLevel}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCurrentSchemaPriviLevel(SpeakQlParser.CurrentSchemaPriviLevelContext ctx);
	/**
	 * Visit a parse tree produced by the {@code globalPrivLevel}
	 * labeled alternative in {@link SpeakQlParser#privilegeLevel}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitGlobalPrivLevel(SpeakQlParser.GlobalPrivLevelContext ctx);
	/**
	 * Visit a parse tree produced by the {@code definiteSchemaPrivLevel}
	 * labeled alternative in {@link SpeakQlParser#privilegeLevel}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDefiniteSchemaPrivLevel(SpeakQlParser.DefiniteSchemaPrivLevelContext ctx);
	/**
	 * Visit a parse tree produced by the {@code definiteFullTablePrivLevel}
	 * labeled alternative in {@link SpeakQlParser#privilegeLevel}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDefiniteFullTablePrivLevel(SpeakQlParser.DefiniteFullTablePrivLevelContext ctx);
	/**
	 * Visit a parse tree produced by the {@code definiteFullTablePrivLevel2}
	 * labeled alternative in {@link SpeakQlParser#privilegeLevel}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDefiniteFullTablePrivLevel2(SpeakQlParser.DefiniteFullTablePrivLevel2Context ctx);
	/**
	 * Visit a parse tree produced by the {@code definiteTablePrivLevel}
	 * labeled alternative in {@link SpeakQlParser#privilegeLevel}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDefiniteTablePrivLevel(SpeakQlParser.DefiniteTablePrivLevelContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#renameUserClause}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRenameUserClause(SpeakQlParser.RenameUserClauseContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#analyzeTable}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAnalyzeTable(SpeakQlParser.AnalyzeTableContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#checkTable}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCheckTable(SpeakQlParser.CheckTableContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#checksumTable}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitChecksumTable(SpeakQlParser.ChecksumTableContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#optimizeTable}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOptimizeTable(SpeakQlParser.OptimizeTableContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#repairTable}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRepairTable(SpeakQlParser.RepairTableContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#checkTableOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCheckTableOption(SpeakQlParser.CheckTableOptionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#createUdfunction}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCreateUdfunction(SpeakQlParser.CreateUdfunctionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#installPlugin}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInstallPlugin(SpeakQlParser.InstallPluginContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#uninstallPlugin}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUninstallPlugin(SpeakQlParser.UninstallPluginContext ctx);
	/**
	 * Visit a parse tree produced by the {@code setVariable}
	 * labeled alternative in {@link SpeakQlParser#setStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSetVariable(SpeakQlParser.SetVariableContext ctx);
	/**
	 * Visit a parse tree produced by the {@code setCharset}
	 * labeled alternative in {@link SpeakQlParser#setStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSetCharset(SpeakQlParser.SetCharsetContext ctx);
	/**
	 * Visit a parse tree produced by the {@code setNames}
	 * labeled alternative in {@link SpeakQlParser#setStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSetNames(SpeakQlParser.SetNamesContext ctx);
	/**
	 * Visit a parse tree produced by the {@code setPassword}
	 * labeled alternative in {@link SpeakQlParser#setStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSetPassword(SpeakQlParser.SetPasswordContext ctx);
	/**
	 * Visit a parse tree produced by the {@code setTransaction}
	 * labeled alternative in {@link SpeakQlParser#setStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSetTransaction(SpeakQlParser.SetTransactionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code setAutocommit}
	 * labeled alternative in {@link SpeakQlParser#setStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSetAutocommit(SpeakQlParser.SetAutocommitContext ctx);
	/**
	 * Visit a parse tree produced by the {@code setNewValueInsideTrigger}
	 * labeled alternative in {@link SpeakQlParser#setStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSetNewValueInsideTrigger(SpeakQlParser.SetNewValueInsideTriggerContext ctx);
	/**
	 * Visit a parse tree produced by the {@code showMasterLogs}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitShowMasterLogs(SpeakQlParser.ShowMasterLogsContext ctx);
	/**
	 * Visit a parse tree produced by the {@code showLogEvents}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitShowLogEvents(SpeakQlParser.ShowLogEventsContext ctx);
	/**
	 * Visit a parse tree produced by the {@code showObjectFilter}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitShowObjectFilter(SpeakQlParser.ShowObjectFilterContext ctx);
	/**
	 * Visit a parse tree produced by the {@code showColumns}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitShowColumns(SpeakQlParser.ShowColumnsContext ctx);
	/**
	 * Visit a parse tree produced by the {@code showCreateDb}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitShowCreateDb(SpeakQlParser.ShowCreateDbContext ctx);
	/**
	 * Visit a parse tree produced by the {@code showCreateFullIdObject}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitShowCreateFullIdObject(SpeakQlParser.ShowCreateFullIdObjectContext ctx);
	/**
	 * Visit a parse tree produced by the {@code showCreateUser}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitShowCreateUser(SpeakQlParser.ShowCreateUserContext ctx);
	/**
	 * Visit a parse tree produced by the {@code showEngine}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitShowEngine(SpeakQlParser.ShowEngineContext ctx);
	/**
	 * Visit a parse tree produced by the {@code showGlobalInfo}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitShowGlobalInfo(SpeakQlParser.ShowGlobalInfoContext ctx);
	/**
	 * Visit a parse tree produced by the {@code showErrors}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitShowErrors(SpeakQlParser.ShowErrorsContext ctx);
	/**
	 * Visit a parse tree produced by the {@code showCountErrors}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitShowCountErrors(SpeakQlParser.ShowCountErrorsContext ctx);
	/**
	 * Visit a parse tree produced by the {@code showSchemaFilter}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitShowSchemaFilter(SpeakQlParser.ShowSchemaFilterContext ctx);
	/**
	 * Visit a parse tree produced by the {@code showRoutine}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitShowRoutine(SpeakQlParser.ShowRoutineContext ctx);
	/**
	 * Visit a parse tree produced by the {@code showGrants}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitShowGrants(SpeakQlParser.ShowGrantsContext ctx);
	/**
	 * Visit a parse tree produced by the {@code showIndexes}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitShowIndexes(SpeakQlParser.ShowIndexesContext ctx);
	/**
	 * Visit a parse tree produced by the {@code showOpenTables}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitShowOpenTables(SpeakQlParser.ShowOpenTablesContext ctx);
	/**
	 * Visit a parse tree produced by the {@code showProfile}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitShowProfile(SpeakQlParser.ShowProfileContext ctx);
	/**
	 * Visit a parse tree produced by the {@code showSlaveStatus}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitShowSlaveStatus(SpeakQlParser.ShowSlaveStatusContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#variableClause}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVariableClause(SpeakQlParser.VariableClauseContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#showCommonEntity}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitShowCommonEntity(SpeakQlParser.ShowCommonEntityContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#showFilter}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitShowFilter(SpeakQlParser.ShowFilterContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#showGlobalInfoClause}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitShowGlobalInfoClause(SpeakQlParser.ShowGlobalInfoClauseContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#showSchemaEntity}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitShowSchemaEntity(SpeakQlParser.ShowSchemaEntityContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#showProfileType}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitShowProfileType(SpeakQlParser.ShowProfileTypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#binlogStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBinlogStatement(SpeakQlParser.BinlogStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#cacheIndexStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCacheIndexStatement(SpeakQlParser.CacheIndexStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#flushStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFlushStatement(SpeakQlParser.FlushStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#killStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitKillStatement(SpeakQlParser.KillStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#loadIndexIntoCache}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLoadIndexIntoCache(SpeakQlParser.LoadIndexIntoCacheContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#resetStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitResetStatement(SpeakQlParser.ResetStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#shutdownStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitShutdownStatement(SpeakQlParser.ShutdownStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#tableIndexes}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableIndexes(SpeakQlParser.TableIndexesContext ctx);
	/**
	 * Visit a parse tree produced by the {@code simpleFlushOption}
	 * labeled alternative in {@link SpeakQlParser#flushOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSimpleFlushOption(SpeakQlParser.SimpleFlushOptionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code channelFlushOption}
	 * labeled alternative in {@link SpeakQlParser#flushOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitChannelFlushOption(SpeakQlParser.ChannelFlushOptionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tableFlushOption}
	 * labeled alternative in {@link SpeakQlParser#flushOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableFlushOption(SpeakQlParser.TableFlushOptionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#flushTableOption}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFlushTableOption(SpeakQlParser.FlushTableOptionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#loadedTableIndexes}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLoadedTableIndexes(SpeakQlParser.LoadedTableIndexesContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#simpleDescribeStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSimpleDescribeStatement(SpeakQlParser.SimpleDescribeStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#fullDescribeStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFullDescribeStatement(SpeakQlParser.FullDescribeStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#helpStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitHelpStatement(SpeakQlParser.HelpStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#useStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUseStatement(SpeakQlParser.UseStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#signalStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSignalStatement(SpeakQlParser.SignalStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#resignalStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitResignalStatement(SpeakQlParser.ResignalStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#signalConditionInformation}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSignalConditionInformation(SpeakQlParser.SignalConditionInformationContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#diagnosticsStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDiagnosticsStatement(SpeakQlParser.DiagnosticsStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#diagnosticsConditionInformationName}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDiagnosticsConditionInformationName(SpeakQlParser.DiagnosticsConditionInformationNameContext ctx);
	/**
	 * Visit a parse tree produced by the {@code describeStatements}
	 * labeled alternative in {@link SpeakQlParser#describeObjectClause}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDescribeStatements(SpeakQlParser.DescribeStatementsContext ctx);
	/**
	 * Visit a parse tree produced by the {@code describeConnection}
	 * labeled alternative in {@link SpeakQlParser#describeObjectClause}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDescribeConnection(SpeakQlParser.DescribeConnectionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#fullId}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFullId(SpeakQlParser.FullIdContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#tableName}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTableName(SpeakQlParser.TableNameContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#fullColumnName}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFullColumnName(SpeakQlParser.FullColumnNameContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#indexColumnName}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIndexColumnName(SpeakQlParser.IndexColumnNameContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#userName}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUserName(SpeakQlParser.UserNameContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#mysqlVariable}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMysqlVariable(SpeakQlParser.MysqlVariableContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#charsetName}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCharsetName(SpeakQlParser.CharsetNameContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#collationName}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCollationName(SpeakQlParser.CollationNameContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#engineName}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEngineName(SpeakQlParser.EngineNameContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#uuidSet}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUuidSet(SpeakQlParser.UuidSetContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#xid}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitXid(SpeakQlParser.XidContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#xuidStringId}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitXuidStringId(SpeakQlParser.XuidStringIdContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#authPlugin}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAuthPlugin(SpeakQlParser.AuthPluginContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#uid}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUid(SpeakQlParser.UidContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#simpleId}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSimpleId(SpeakQlParser.SimpleIdContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#dottedId}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDottedId(SpeakQlParser.DottedIdContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#decimalLiteral}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDecimalLiteral(SpeakQlParser.DecimalLiteralContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#fileSizeLiteral}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFileSizeLiteral(SpeakQlParser.FileSizeLiteralContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#stringLiteral}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStringLiteral(SpeakQlParser.StringLiteralContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#booleanLiteral}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBooleanLiteral(SpeakQlParser.BooleanLiteralContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#hexadecimalLiteral}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitHexadecimalLiteral(SpeakQlParser.HexadecimalLiteralContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#nullNotnull}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNullNotnull(SpeakQlParser.NullNotnullContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#constant}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitConstant(SpeakQlParser.ConstantContext ctx);
	/**
	 * Visit a parse tree produced by the {@code stringDataType}
	 * labeled alternative in {@link SpeakQlParser#dataType}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStringDataType(SpeakQlParser.StringDataTypeContext ctx);
	/**
	 * Visit a parse tree produced by the {@code nationalStringDataType}
	 * labeled alternative in {@link SpeakQlParser#dataType}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNationalStringDataType(SpeakQlParser.NationalStringDataTypeContext ctx);
	/**
	 * Visit a parse tree produced by the {@code nationalVaryingStringDataType}
	 * labeled alternative in {@link SpeakQlParser#dataType}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNationalVaryingStringDataType(SpeakQlParser.NationalVaryingStringDataTypeContext ctx);
	/**
	 * Visit a parse tree produced by the {@code dimensionDataType}
	 * labeled alternative in {@link SpeakQlParser#dataType}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDimensionDataType(SpeakQlParser.DimensionDataTypeContext ctx);
	/**
	 * Visit a parse tree produced by the {@code simpleDataType}
	 * labeled alternative in {@link SpeakQlParser#dataType}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSimpleDataType(SpeakQlParser.SimpleDataTypeContext ctx);
	/**
	 * Visit a parse tree produced by the {@code collectionDataType}
	 * labeled alternative in {@link SpeakQlParser#dataType}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCollectionDataType(SpeakQlParser.CollectionDataTypeContext ctx);
	/**
	 * Visit a parse tree produced by the {@code spatialDataType}
	 * labeled alternative in {@link SpeakQlParser#dataType}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSpatialDataType(SpeakQlParser.SpatialDataTypeContext ctx);
	/**
	 * Visit a parse tree produced by the {@code longVarcharDataType}
	 * labeled alternative in {@link SpeakQlParser#dataType}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLongVarcharDataType(SpeakQlParser.LongVarcharDataTypeContext ctx);
	/**
	 * Visit a parse tree produced by the {@code longVarbinaryDataType}
	 * labeled alternative in {@link SpeakQlParser#dataType}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLongVarbinaryDataType(SpeakQlParser.LongVarbinaryDataTypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#collectionOptions}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCollectionOptions(SpeakQlParser.CollectionOptionsContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#convertedDataType}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitConvertedDataType(SpeakQlParser.ConvertedDataTypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#lengthOneDimension}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLengthOneDimension(SpeakQlParser.LengthOneDimensionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#lengthTwoDimension}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLengthTwoDimension(SpeakQlParser.LengthTwoDimensionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#lengthTwoOptionalDimension}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLengthTwoOptionalDimension(SpeakQlParser.LengthTwoOptionalDimensionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#uidList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUidList(SpeakQlParser.UidListContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#tables}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTables(SpeakQlParser.TablesContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#indexColumnNames}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIndexColumnNames(SpeakQlParser.IndexColumnNamesContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#expressions}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpressions(SpeakQlParser.ExpressionsContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#expressionsWithDefaults}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpressionsWithDefaults(SpeakQlParser.ExpressionsWithDefaultsContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#constants}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitConstants(SpeakQlParser.ConstantsContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#simpleStrings}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSimpleStrings(SpeakQlParser.SimpleStringsContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#userVariables}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUserVariables(SpeakQlParser.UserVariablesContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#defaultValue}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDefaultValue(SpeakQlParser.DefaultValueContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#currentTimestamp}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCurrentTimestamp(SpeakQlParser.CurrentTimestampContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#expressionOrDefault}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpressionOrDefault(SpeakQlParser.ExpressionOrDefaultContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#ifExists}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIfExists(SpeakQlParser.IfExistsContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#ifNotExists}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIfNotExists(SpeakQlParser.IfNotExistsContext ctx);
	/**
	 * Visit a parse tree produced by the {@code specificFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#functionCall}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSpecificFunctionCall(SpeakQlParser.SpecificFunctionCallContext ctx);
	/**
	 * Visit a parse tree produced by the {@code aggregateFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#functionCall}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAggregateFunctionCall(SpeakQlParser.AggregateFunctionCallContext ctx);
	/**
	 * Visit a parse tree produced by the {@code nonAggregateFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#functionCall}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNonAggregateFunctionCall(SpeakQlParser.NonAggregateFunctionCallContext ctx);
	/**
	 * Visit a parse tree produced by the {@code scalarFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#functionCall}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitScalarFunctionCall(SpeakQlParser.ScalarFunctionCallContext ctx);
	/**
	 * Visit a parse tree produced by the {@code udfFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#functionCall}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUdfFunctionCall(SpeakQlParser.UdfFunctionCallContext ctx);
	/**
	 * Visit a parse tree produced by the {@code passwordFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#functionCall}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPasswordFunctionCall(SpeakQlParser.PasswordFunctionCallContext ctx);
	/**
	 * Visit a parse tree produced by the {@code simpleFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSimpleFunctionCall(SpeakQlParser.SimpleFunctionCallContext ctx);
	/**
	 * Visit a parse tree produced by the {@code dataTypeFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDataTypeFunctionCall(SpeakQlParser.DataTypeFunctionCallContext ctx);
	/**
	 * Visit a parse tree produced by the {@code valuesFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitValuesFunctionCall(SpeakQlParser.ValuesFunctionCallContext ctx);
	/**
	 * Visit a parse tree produced by the {@code caseExpressionFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCaseExpressionFunctionCall(SpeakQlParser.CaseExpressionFunctionCallContext ctx);
	/**
	 * Visit a parse tree produced by the {@code caseFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCaseFunctionCall(SpeakQlParser.CaseFunctionCallContext ctx);
	/**
	 * Visit a parse tree produced by the {@code charFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCharFunctionCall(SpeakQlParser.CharFunctionCallContext ctx);
	/**
	 * Visit a parse tree produced by the {@code positionFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPositionFunctionCall(SpeakQlParser.PositionFunctionCallContext ctx);
	/**
	 * Visit a parse tree produced by the {@code substrFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSubstrFunctionCall(SpeakQlParser.SubstrFunctionCallContext ctx);
	/**
	 * Visit a parse tree produced by the {@code trimFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTrimFunctionCall(SpeakQlParser.TrimFunctionCallContext ctx);
	/**
	 * Visit a parse tree produced by the {@code weightFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWeightFunctionCall(SpeakQlParser.WeightFunctionCallContext ctx);
	/**
	 * Visit a parse tree produced by the {@code extractFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExtractFunctionCall(SpeakQlParser.ExtractFunctionCallContext ctx);
	/**
	 * Visit a parse tree produced by the {@code getFormatFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitGetFormatFunctionCall(SpeakQlParser.GetFormatFunctionCallContext ctx);
	/**
	 * Visit a parse tree produced by the {@code jsonValueFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitJsonValueFunctionCall(SpeakQlParser.JsonValueFunctionCallContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#caseFuncAlternative}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCaseFuncAlternative(SpeakQlParser.CaseFuncAlternativeContext ctx);
	/**
	 * Visit a parse tree produced by the {@code levelWeightList}
	 * labeled alternative in {@link SpeakQlParser#levelsInWeightString}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLevelWeightList(SpeakQlParser.LevelWeightListContext ctx);
	/**
	 * Visit a parse tree produced by the {@code levelWeightRange}
	 * labeled alternative in {@link SpeakQlParser#levelsInWeightString}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLevelWeightRange(SpeakQlParser.LevelWeightRangeContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#levelInWeightListElement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLevelInWeightListElement(SpeakQlParser.LevelInWeightListElementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#aggregateWindowedFunction}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAggregateWindowedFunction(SpeakQlParser.AggregateWindowedFunctionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#nonAggregateWindowedFunction}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNonAggregateWindowedFunction(SpeakQlParser.NonAggregateWindowedFunctionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#overClause}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOverClause(SpeakQlParser.OverClauseContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#windowSpec}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWindowSpec(SpeakQlParser.WindowSpecContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#windowName}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWindowName(SpeakQlParser.WindowNameContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#frameClause}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFrameClause(SpeakQlParser.FrameClauseContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#frameUnits}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFrameUnits(SpeakQlParser.FrameUnitsContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#frameExtent}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFrameExtent(SpeakQlParser.FrameExtentContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#frameBetween}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFrameBetween(SpeakQlParser.FrameBetweenContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#frameRange}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFrameRange(SpeakQlParser.FrameRangeContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#partitionClause}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPartitionClause(SpeakQlParser.PartitionClauseContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#scalarFunctionName}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitScalarFunctionName(SpeakQlParser.ScalarFunctionNameContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#passwordFunctionClause}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPasswordFunctionClause(SpeakQlParser.PasswordFunctionClauseContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#functionArgs}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunctionArgs(SpeakQlParser.FunctionArgsContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#functionArg}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunctionArg(SpeakQlParser.FunctionArgContext ctx);
	/**
	 * Visit a parse tree produced by the {@code isExpression}
	 * labeled alternative in {@link SpeakQlParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIsExpression(SpeakQlParser.IsExpressionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code notExpression}
	 * labeled alternative in {@link SpeakQlParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNotExpression(SpeakQlParser.NotExpressionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code logicalExpression}
	 * labeled alternative in {@link SpeakQlParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLogicalExpression(SpeakQlParser.LogicalExpressionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code predicateExpression}
	 * labeled alternative in {@link SpeakQlParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPredicateExpression(SpeakQlParser.PredicateExpressionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code soundsLikePredicate}
	 * labeled alternative in {@link SpeakQlParser#predicate}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSoundsLikePredicate(SpeakQlParser.SoundsLikePredicateContext ctx);
	/**
	 * Visit a parse tree produced by the {@code expressionAtomPredicate}
	 * labeled alternative in {@link SpeakQlParser#predicate}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpressionAtomPredicate(SpeakQlParser.ExpressionAtomPredicateContext ctx);
	/**
	 * Visit a parse tree produced by the {@code subqueryComparisonPredicate}
	 * labeled alternative in {@link SpeakQlParser#predicate}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSubqueryComparisonPredicate(SpeakQlParser.SubqueryComparisonPredicateContext ctx);
	/**
	 * Visit a parse tree produced by the {@code jsonMemberOfPredicate}
	 * labeled alternative in {@link SpeakQlParser#predicate}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitJsonMemberOfPredicate(SpeakQlParser.JsonMemberOfPredicateContext ctx);
	/**
	 * Visit a parse tree produced by the {@code binaryComparisonPredicate}
	 * labeled alternative in {@link SpeakQlParser#predicate}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBinaryComparisonPredicate(SpeakQlParser.BinaryComparisonPredicateContext ctx);
	/**
	 * Visit a parse tree produced by the {@code inPredicate}
	 * labeled alternative in {@link SpeakQlParser#predicate}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInPredicate(SpeakQlParser.InPredicateContext ctx);
	/**
	 * Visit a parse tree produced by the {@code betweenPredicate}
	 * labeled alternative in {@link SpeakQlParser#predicate}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBetweenPredicate(SpeakQlParser.BetweenPredicateContext ctx);
	/**
	 * Visit a parse tree produced by the {@code isNullPredicate}
	 * labeled alternative in {@link SpeakQlParser#predicate}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIsNullPredicate(SpeakQlParser.IsNullPredicateContext ctx);
	/**
	 * Visit a parse tree produced by the {@code likePredicate}
	 * labeled alternative in {@link SpeakQlParser#predicate}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLikePredicate(SpeakQlParser.LikePredicateContext ctx);
	/**
	 * Visit a parse tree produced by the {@code regexpPredicate}
	 * labeled alternative in {@link SpeakQlParser#predicate}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRegexpPredicate(SpeakQlParser.RegexpPredicateContext ctx);
	/**
	 * Visit a parse tree produced by the {@code unaryExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUnaryExpressionAtom(SpeakQlParser.UnaryExpressionAtomContext ctx);
	/**
	 * Visit a parse tree produced by the {@code collateExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCollateExpressionAtom(SpeakQlParser.CollateExpressionAtomContext ctx);
	/**
	 * Visit a parse tree produced by the {@code mysqlVariableExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMysqlVariableExpressionAtom(SpeakQlParser.MysqlVariableExpressionAtomContext ctx);
	/**
	 * Visit a parse tree produced by the {@code nestedExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNestedExpressionAtom(SpeakQlParser.NestedExpressionAtomContext ctx);
	/**
	 * Visit a parse tree produced by the {@code nestedRowExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNestedRowExpressionAtom(SpeakQlParser.NestedRowExpressionAtomContext ctx);
	/**
	 * Visit a parse tree produced by the {@code mathExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMathExpressionAtom(SpeakQlParser.MathExpressionAtomContext ctx);
	/**
	 * Visit a parse tree produced by the {@code existsExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExistsExpressionAtom(SpeakQlParser.ExistsExpressionAtomContext ctx);
	/**
	 * Visit a parse tree produced by the {@code intervalExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIntervalExpressionAtom(SpeakQlParser.IntervalExpressionAtomContext ctx);
	/**
	 * Visit a parse tree produced by the {@code jsonExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitJsonExpressionAtom(SpeakQlParser.JsonExpressionAtomContext ctx);
	/**
	 * Visit a parse tree produced by the {@code subqueryExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSubqueryExpressionAtom(SpeakQlParser.SubqueryExpressionAtomContext ctx);
	/**
	 * Visit a parse tree produced by the {@code constantExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitConstantExpressionAtom(SpeakQlParser.ConstantExpressionAtomContext ctx);
	/**
	 * Visit a parse tree produced by the {@code functionCallExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunctionCallExpressionAtom(SpeakQlParser.FunctionCallExpressionAtomContext ctx);
	/**
	 * Visit a parse tree produced by the {@code binaryExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBinaryExpressionAtom(SpeakQlParser.BinaryExpressionAtomContext ctx);
	/**
	 * Visit a parse tree produced by the {@code fullColumnNameExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFullColumnNameExpressionAtom(SpeakQlParser.FullColumnNameExpressionAtomContext ctx);
	/**
	 * Visit a parse tree produced by the {@code bitExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBitExpressionAtom(SpeakQlParser.BitExpressionAtomContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#unaryOperator}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUnaryOperator(SpeakQlParser.UnaryOperatorContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#comparisonOperator}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitComparisonOperator(SpeakQlParser.ComparisonOperatorContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#logicalOperator}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLogicalOperator(SpeakQlParser.LogicalOperatorContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#bitOperator}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBitOperator(SpeakQlParser.BitOperatorContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#mathOperator}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMathOperator(SpeakQlParser.MathOperatorContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#jsonOperator}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitJsonOperator(SpeakQlParser.JsonOperatorContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#charsetNameBase}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCharsetNameBase(SpeakQlParser.CharsetNameBaseContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#transactionLevelBase}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTransactionLevelBase(SpeakQlParser.TransactionLevelBaseContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#privilegesBase}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrivilegesBase(SpeakQlParser.PrivilegesBaseContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#intervalTypeBase}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIntervalTypeBase(SpeakQlParser.IntervalTypeBaseContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#dataTypeBase}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDataTypeBase(SpeakQlParser.DataTypeBaseContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#keywordsCanBeId}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitKeywordsCanBeId(SpeakQlParser.KeywordsCanBeIdContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpeakQlParser#functionNameBase}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunctionNameBase(SpeakQlParser.FunctionNameBaseContext ctx);
}
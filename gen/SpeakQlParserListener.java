// Generated from C:/antlr_projects/speakql2\SpeakQlParser.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link SpeakQlParser}.
 */
public interface SpeakQlParserListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#root}.
	 * @param ctx the parse tree
	 */
	void enterRoot(SpeakQlParser.RootContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#root}.
	 * @param ctx the parse tree
	 */
	void exitRoot(SpeakQlParser.RootContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#sqlStatements}.
	 * @param ctx the parse tree
	 */
	void enterSqlStatements(SpeakQlParser.SqlStatementsContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#sqlStatements}.
	 * @param ctx the parse tree
	 */
	void exitSqlStatements(SpeakQlParser.SqlStatementsContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#sqlStatement}.
	 * @param ctx the parse tree
	 */
	void enterSqlStatement(SpeakQlParser.SqlStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#sqlStatement}.
	 * @param ctx the parse tree
	 */
	void exitSqlStatement(SpeakQlParser.SqlStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#emptyStatement}.
	 * @param ctx the parse tree
	 */
	void enterEmptyStatement(SpeakQlParser.EmptyStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#emptyStatement}.
	 * @param ctx the parse tree
	 */
	void exitEmptyStatement(SpeakQlParser.EmptyStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#ddlStatement}.
	 * @param ctx the parse tree
	 */
	void enterDdlStatement(SpeakQlParser.DdlStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#ddlStatement}.
	 * @param ctx the parse tree
	 */
	void exitDdlStatement(SpeakQlParser.DdlStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#dmlStatement}.
	 * @param ctx the parse tree
	 */
	void enterDmlStatement(SpeakQlParser.DmlStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#dmlStatement}.
	 * @param ctx the parse tree
	 */
	void exitDmlStatement(SpeakQlParser.DmlStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#transactionStatement}.
	 * @param ctx the parse tree
	 */
	void enterTransactionStatement(SpeakQlParser.TransactionStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#transactionStatement}.
	 * @param ctx the parse tree
	 */
	void exitTransactionStatement(SpeakQlParser.TransactionStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#replicationStatement}.
	 * @param ctx the parse tree
	 */
	void enterReplicationStatement(SpeakQlParser.ReplicationStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#replicationStatement}.
	 * @param ctx the parse tree
	 */
	void exitReplicationStatement(SpeakQlParser.ReplicationStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#preparedStatement}.
	 * @param ctx the parse tree
	 */
	void enterPreparedStatement(SpeakQlParser.PreparedStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#preparedStatement}.
	 * @param ctx the parse tree
	 */
	void exitPreparedStatement(SpeakQlParser.PreparedStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#compoundStatement}.
	 * @param ctx the parse tree
	 */
	void enterCompoundStatement(SpeakQlParser.CompoundStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#compoundStatement}.
	 * @param ctx the parse tree
	 */
	void exitCompoundStatement(SpeakQlParser.CompoundStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#administrationStatement}.
	 * @param ctx the parse tree
	 */
	void enterAdministrationStatement(SpeakQlParser.AdministrationStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#administrationStatement}.
	 * @param ctx the parse tree
	 */
	void exitAdministrationStatement(SpeakQlParser.AdministrationStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#utilityStatement}.
	 * @param ctx the parse tree
	 */
	void enterUtilityStatement(SpeakQlParser.UtilityStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#utilityStatement}.
	 * @param ctx the parse tree
	 */
	void exitUtilityStatement(SpeakQlParser.UtilityStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#createDatabase}.
	 * @param ctx the parse tree
	 */
	void enterCreateDatabase(SpeakQlParser.CreateDatabaseContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#createDatabase}.
	 * @param ctx the parse tree
	 */
	void exitCreateDatabase(SpeakQlParser.CreateDatabaseContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#createEvent}.
	 * @param ctx the parse tree
	 */
	void enterCreateEvent(SpeakQlParser.CreateEventContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#createEvent}.
	 * @param ctx the parse tree
	 */
	void exitCreateEvent(SpeakQlParser.CreateEventContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#createIndex}.
	 * @param ctx the parse tree
	 */
	void enterCreateIndex(SpeakQlParser.CreateIndexContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#createIndex}.
	 * @param ctx the parse tree
	 */
	void exitCreateIndex(SpeakQlParser.CreateIndexContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#createLogfileGroup}.
	 * @param ctx the parse tree
	 */
	void enterCreateLogfileGroup(SpeakQlParser.CreateLogfileGroupContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#createLogfileGroup}.
	 * @param ctx the parse tree
	 */
	void exitCreateLogfileGroup(SpeakQlParser.CreateLogfileGroupContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#createProcedure}.
	 * @param ctx the parse tree
	 */
	void enterCreateProcedure(SpeakQlParser.CreateProcedureContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#createProcedure}.
	 * @param ctx the parse tree
	 */
	void exitCreateProcedure(SpeakQlParser.CreateProcedureContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#createFunction}.
	 * @param ctx the parse tree
	 */
	void enterCreateFunction(SpeakQlParser.CreateFunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#createFunction}.
	 * @param ctx the parse tree
	 */
	void exitCreateFunction(SpeakQlParser.CreateFunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#createServer}.
	 * @param ctx the parse tree
	 */
	void enterCreateServer(SpeakQlParser.CreateServerContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#createServer}.
	 * @param ctx the parse tree
	 */
	void exitCreateServer(SpeakQlParser.CreateServerContext ctx);
	/**
	 * Enter a parse tree produced by the {@code copyCreateTable}
	 * labeled alternative in {@link SpeakQlParser#createTable}.
	 * @param ctx the parse tree
	 */
	void enterCopyCreateTable(SpeakQlParser.CopyCreateTableContext ctx);
	/**
	 * Exit a parse tree produced by the {@code copyCreateTable}
	 * labeled alternative in {@link SpeakQlParser#createTable}.
	 * @param ctx the parse tree
	 */
	void exitCopyCreateTable(SpeakQlParser.CopyCreateTableContext ctx);
	/**
	 * Enter a parse tree produced by the {@code queryCreateTable}
	 * labeled alternative in {@link SpeakQlParser#createTable}.
	 * @param ctx the parse tree
	 */
	void enterQueryCreateTable(SpeakQlParser.QueryCreateTableContext ctx);
	/**
	 * Exit a parse tree produced by the {@code queryCreateTable}
	 * labeled alternative in {@link SpeakQlParser#createTable}.
	 * @param ctx the parse tree
	 */
	void exitQueryCreateTable(SpeakQlParser.QueryCreateTableContext ctx);
	/**
	 * Enter a parse tree produced by the {@code columnCreateTable}
	 * labeled alternative in {@link SpeakQlParser#createTable}.
	 * @param ctx the parse tree
	 */
	void enterColumnCreateTable(SpeakQlParser.ColumnCreateTableContext ctx);
	/**
	 * Exit a parse tree produced by the {@code columnCreateTable}
	 * labeled alternative in {@link SpeakQlParser#createTable}.
	 * @param ctx the parse tree
	 */
	void exitColumnCreateTable(SpeakQlParser.ColumnCreateTableContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#createTablespaceInnodb}.
	 * @param ctx the parse tree
	 */
	void enterCreateTablespaceInnodb(SpeakQlParser.CreateTablespaceInnodbContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#createTablespaceInnodb}.
	 * @param ctx the parse tree
	 */
	void exitCreateTablespaceInnodb(SpeakQlParser.CreateTablespaceInnodbContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#createTablespaceNdb}.
	 * @param ctx the parse tree
	 */
	void enterCreateTablespaceNdb(SpeakQlParser.CreateTablespaceNdbContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#createTablespaceNdb}.
	 * @param ctx the parse tree
	 */
	void exitCreateTablespaceNdb(SpeakQlParser.CreateTablespaceNdbContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#createTrigger}.
	 * @param ctx the parse tree
	 */
	void enterCreateTrigger(SpeakQlParser.CreateTriggerContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#createTrigger}.
	 * @param ctx the parse tree
	 */
	void exitCreateTrigger(SpeakQlParser.CreateTriggerContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#createView}.
	 * @param ctx the parse tree
	 */
	void enterCreateView(SpeakQlParser.CreateViewContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#createView}.
	 * @param ctx the parse tree
	 */
	void exitCreateView(SpeakQlParser.CreateViewContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#createDatabaseOption}.
	 * @param ctx the parse tree
	 */
	void enterCreateDatabaseOption(SpeakQlParser.CreateDatabaseOptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#createDatabaseOption}.
	 * @param ctx the parse tree
	 */
	void exitCreateDatabaseOption(SpeakQlParser.CreateDatabaseOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#ownerStatement}.
	 * @param ctx the parse tree
	 */
	void enterOwnerStatement(SpeakQlParser.OwnerStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#ownerStatement}.
	 * @param ctx the parse tree
	 */
	void exitOwnerStatement(SpeakQlParser.OwnerStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code preciseSchedule}
	 * labeled alternative in {@link SpeakQlParser#scheduleExpression}.
	 * @param ctx the parse tree
	 */
	void enterPreciseSchedule(SpeakQlParser.PreciseScheduleContext ctx);
	/**
	 * Exit a parse tree produced by the {@code preciseSchedule}
	 * labeled alternative in {@link SpeakQlParser#scheduleExpression}.
	 * @param ctx the parse tree
	 */
	void exitPreciseSchedule(SpeakQlParser.PreciseScheduleContext ctx);
	/**
	 * Enter a parse tree produced by the {@code intervalSchedule}
	 * labeled alternative in {@link SpeakQlParser#scheduleExpression}.
	 * @param ctx the parse tree
	 */
	void enterIntervalSchedule(SpeakQlParser.IntervalScheduleContext ctx);
	/**
	 * Exit a parse tree produced by the {@code intervalSchedule}
	 * labeled alternative in {@link SpeakQlParser#scheduleExpression}.
	 * @param ctx the parse tree
	 */
	void exitIntervalSchedule(SpeakQlParser.IntervalScheduleContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#timestampValue}.
	 * @param ctx the parse tree
	 */
	void enterTimestampValue(SpeakQlParser.TimestampValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#timestampValue}.
	 * @param ctx the parse tree
	 */
	void exitTimestampValue(SpeakQlParser.TimestampValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#intervalExpr}.
	 * @param ctx the parse tree
	 */
	void enterIntervalExpr(SpeakQlParser.IntervalExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#intervalExpr}.
	 * @param ctx the parse tree
	 */
	void exitIntervalExpr(SpeakQlParser.IntervalExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#intervalType}.
	 * @param ctx the parse tree
	 */
	void enterIntervalType(SpeakQlParser.IntervalTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#intervalType}.
	 * @param ctx the parse tree
	 */
	void exitIntervalType(SpeakQlParser.IntervalTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#enableType}.
	 * @param ctx the parse tree
	 */
	void enterEnableType(SpeakQlParser.EnableTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#enableType}.
	 * @param ctx the parse tree
	 */
	void exitEnableType(SpeakQlParser.EnableTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#indexType}.
	 * @param ctx the parse tree
	 */
	void enterIndexType(SpeakQlParser.IndexTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#indexType}.
	 * @param ctx the parse tree
	 */
	void exitIndexType(SpeakQlParser.IndexTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#indexOption}.
	 * @param ctx the parse tree
	 */
	void enterIndexOption(SpeakQlParser.IndexOptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#indexOption}.
	 * @param ctx the parse tree
	 */
	void exitIndexOption(SpeakQlParser.IndexOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#procedureParameter}.
	 * @param ctx the parse tree
	 */
	void enterProcedureParameter(SpeakQlParser.ProcedureParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#procedureParameter}.
	 * @param ctx the parse tree
	 */
	void exitProcedureParameter(SpeakQlParser.ProcedureParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#functionParameter}.
	 * @param ctx the parse tree
	 */
	void enterFunctionParameter(SpeakQlParser.FunctionParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#functionParameter}.
	 * @param ctx the parse tree
	 */
	void exitFunctionParameter(SpeakQlParser.FunctionParameterContext ctx);
	/**
	 * Enter a parse tree produced by the {@code routineComment}
	 * labeled alternative in {@link SpeakQlParser#routineOption}.
	 * @param ctx the parse tree
	 */
	void enterRoutineComment(SpeakQlParser.RoutineCommentContext ctx);
	/**
	 * Exit a parse tree produced by the {@code routineComment}
	 * labeled alternative in {@link SpeakQlParser#routineOption}.
	 * @param ctx the parse tree
	 */
	void exitRoutineComment(SpeakQlParser.RoutineCommentContext ctx);
	/**
	 * Enter a parse tree produced by the {@code routineLanguage}
	 * labeled alternative in {@link SpeakQlParser#routineOption}.
	 * @param ctx the parse tree
	 */
	void enterRoutineLanguage(SpeakQlParser.RoutineLanguageContext ctx);
	/**
	 * Exit a parse tree produced by the {@code routineLanguage}
	 * labeled alternative in {@link SpeakQlParser#routineOption}.
	 * @param ctx the parse tree
	 */
	void exitRoutineLanguage(SpeakQlParser.RoutineLanguageContext ctx);
	/**
	 * Enter a parse tree produced by the {@code routineBehavior}
	 * labeled alternative in {@link SpeakQlParser#routineOption}.
	 * @param ctx the parse tree
	 */
	void enterRoutineBehavior(SpeakQlParser.RoutineBehaviorContext ctx);
	/**
	 * Exit a parse tree produced by the {@code routineBehavior}
	 * labeled alternative in {@link SpeakQlParser#routineOption}.
	 * @param ctx the parse tree
	 */
	void exitRoutineBehavior(SpeakQlParser.RoutineBehaviorContext ctx);
	/**
	 * Enter a parse tree produced by the {@code routineData}
	 * labeled alternative in {@link SpeakQlParser#routineOption}.
	 * @param ctx the parse tree
	 */
	void enterRoutineData(SpeakQlParser.RoutineDataContext ctx);
	/**
	 * Exit a parse tree produced by the {@code routineData}
	 * labeled alternative in {@link SpeakQlParser#routineOption}.
	 * @param ctx the parse tree
	 */
	void exitRoutineData(SpeakQlParser.RoutineDataContext ctx);
	/**
	 * Enter a parse tree produced by the {@code routineSecurity}
	 * labeled alternative in {@link SpeakQlParser#routineOption}.
	 * @param ctx the parse tree
	 */
	void enterRoutineSecurity(SpeakQlParser.RoutineSecurityContext ctx);
	/**
	 * Exit a parse tree produced by the {@code routineSecurity}
	 * labeled alternative in {@link SpeakQlParser#routineOption}.
	 * @param ctx the parse tree
	 */
	void exitRoutineSecurity(SpeakQlParser.RoutineSecurityContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#serverOption}.
	 * @param ctx the parse tree
	 */
	void enterServerOption(SpeakQlParser.ServerOptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#serverOption}.
	 * @param ctx the parse tree
	 */
	void exitServerOption(SpeakQlParser.ServerOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#createDefinitions}.
	 * @param ctx the parse tree
	 */
	void enterCreateDefinitions(SpeakQlParser.CreateDefinitionsContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#createDefinitions}.
	 * @param ctx the parse tree
	 */
	void exitCreateDefinitions(SpeakQlParser.CreateDefinitionsContext ctx);
	/**
	 * Enter a parse tree produced by the {@code columnDeclaration}
	 * labeled alternative in {@link SpeakQlParser#createDefinition}.
	 * @param ctx the parse tree
	 */
	void enterColumnDeclaration(SpeakQlParser.ColumnDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by the {@code columnDeclaration}
	 * labeled alternative in {@link SpeakQlParser#createDefinition}.
	 * @param ctx the parse tree
	 */
	void exitColumnDeclaration(SpeakQlParser.ColumnDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code constraintDeclaration}
	 * labeled alternative in {@link SpeakQlParser#createDefinition}.
	 * @param ctx the parse tree
	 */
	void enterConstraintDeclaration(SpeakQlParser.ConstraintDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by the {@code constraintDeclaration}
	 * labeled alternative in {@link SpeakQlParser#createDefinition}.
	 * @param ctx the parse tree
	 */
	void exitConstraintDeclaration(SpeakQlParser.ConstraintDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code indexDeclaration}
	 * labeled alternative in {@link SpeakQlParser#createDefinition}.
	 * @param ctx the parse tree
	 */
	void enterIndexDeclaration(SpeakQlParser.IndexDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by the {@code indexDeclaration}
	 * labeled alternative in {@link SpeakQlParser#createDefinition}.
	 * @param ctx the parse tree
	 */
	void exitIndexDeclaration(SpeakQlParser.IndexDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#columnDefinition}.
	 * @param ctx the parse tree
	 */
	void enterColumnDefinition(SpeakQlParser.ColumnDefinitionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#columnDefinition}.
	 * @param ctx the parse tree
	 */
	void exitColumnDefinition(SpeakQlParser.ColumnDefinitionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code nullColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 */
	void enterNullColumnConstraint(SpeakQlParser.NullColumnConstraintContext ctx);
	/**
	 * Exit a parse tree produced by the {@code nullColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 */
	void exitNullColumnConstraint(SpeakQlParser.NullColumnConstraintContext ctx);
	/**
	 * Enter a parse tree produced by the {@code defaultColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 */
	void enterDefaultColumnConstraint(SpeakQlParser.DefaultColumnConstraintContext ctx);
	/**
	 * Exit a parse tree produced by the {@code defaultColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 */
	void exitDefaultColumnConstraint(SpeakQlParser.DefaultColumnConstraintContext ctx);
	/**
	 * Enter a parse tree produced by the {@code visibilityColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 */
	void enterVisibilityColumnConstraint(SpeakQlParser.VisibilityColumnConstraintContext ctx);
	/**
	 * Exit a parse tree produced by the {@code visibilityColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 */
	void exitVisibilityColumnConstraint(SpeakQlParser.VisibilityColumnConstraintContext ctx);
	/**
	 * Enter a parse tree produced by the {@code autoIncrementColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 */
	void enterAutoIncrementColumnConstraint(SpeakQlParser.AutoIncrementColumnConstraintContext ctx);
	/**
	 * Exit a parse tree produced by the {@code autoIncrementColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 */
	void exitAutoIncrementColumnConstraint(SpeakQlParser.AutoIncrementColumnConstraintContext ctx);
	/**
	 * Enter a parse tree produced by the {@code primaryKeyColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 */
	void enterPrimaryKeyColumnConstraint(SpeakQlParser.PrimaryKeyColumnConstraintContext ctx);
	/**
	 * Exit a parse tree produced by the {@code primaryKeyColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 */
	void exitPrimaryKeyColumnConstraint(SpeakQlParser.PrimaryKeyColumnConstraintContext ctx);
	/**
	 * Enter a parse tree produced by the {@code uniqueKeyColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 */
	void enterUniqueKeyColumnConstraint(SpeakQlParser.UniqueKeyColumnConstraintContext ctx);
	/**
	 * Exit a parse tree produced by the {@code uniqueKeyColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 */
	void exitUniqueKeyColumnConstraint(SpeakQlParser.UniqueKeyColumnConstraintContext ctx);
	/**
	 * Enter a parse tree produced by the {@code commentColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 */
	void enterCommentColumnConstraint(SpeakQlParser.CommentColumnConstraintContext ctx);
	/**
	 * Exit a parse tree produced by the {@code commentColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 */
	void exitCommentColumnConstraint(SpeakQlParser.CommentColumnConstraintContext ctx);
	/**
	 * Enter a parse tree produced by the {@code formatColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 */
	void enterFormatColumnConstraint(SpeakQlParser.FormatColumnConstraintContext ctx);
	/**
	 * Exit a parse tree produced by the {@code formatColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 */
	void exitFormatColumnConstraint(SpeakQlParser.FormatColumnConstraintContext ctx);
	/**
	 * Enter a parse tree produced by the {@code storageColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 */
	void enterStorageColumnConstraint(SpeakQlParser.StorageColumnConstraintContext ctx);
	/**
	 * Exit a parse tree produced by the {@code storageColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 */
	void exitStorageColumnConstraint(SpeakQlParser.StorageColumnConstraintContext ctx);
	/**
	 * Enter a parse tree produced by the {@code referenceColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 */
	void enterReferenceColumnConstraint(SpeakQlParser.ReferenceColumnConstraintContext ctx);
	/**
	 * Exit a parse tree produced by the {@code referenceColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 */
	void exitReferenceColumnConstraint(SpeakQlParser.ReferenceColumnConstraintContext ctx);
	/**
	 * Enter a parse tree produced by the {@code collateColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 */
	void enterCollateColumnConstraint(SpeakQlParser.CollateColumnConstraintContext ctx);
	/**
	 * Exit a parse tree produced by the {@code collateColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 */
	void exitCollateColumnConstraint(SpeakQlParser.CollateColumnConstraintContext ctx);
	/**
	 * Enter a parse tree produced by the {@code generatedColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 */
	void enterGeneratedColumnConstraint(SpeakQlParser.GeneratedColumnConstraintContext ctx);
	/**
	 * Exit a parse tree produced by the {@code generatedColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 */
	void exitGeneratedColumnConstraint(SpeakQlParser.GeneratedColumnConstraintContext ctx);
	/**
	 * Enter a parse tree produced by the {@code serialDefaultColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 */
	void enterSerialDefaultColumnConstraint(SpeakQlParser.SerialDefaultColumnConstraintContext ctx);
	/**
	 * Exit a parse tree produced by the {@code serialDefaultColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 */
	void exitSerialDefaultColumnConstraint(SpeakQlParser.SerialDefaultColumnConstraintContext ctx);
	/**
	 * Enter a parse tree produced by the {@code checkColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 */
	void enterCheckColumnConstraint(SpeakQlParser.CheckColumnConstraintContext ctx);
	/**
	 * Exit a parse tree produced by the {@code checkColumnConstraint}
	 * labeled alternative in {@link SpeakQlParser#columnConstraint}.
	 * @param ctx the parse tree
	 */
	void exitCheckColumnConstraint(SpeakQlParser.CheckColumnConstraintContext ctx);
	/**
	 * Enter a parse tree produced by the {@code primaryKeyTableConstraint}
	 * labeled alternative in {@link SpeakQlParser#tableConstraint}.
	 * @param ctx the parse tree
	 */
	void enterPrimaryKeyTableConstraint(SpeakQlParser.PrimaryKeyTableConstraintContext ctx);
	/**
	 * Exit a parse tree produced by the {@code primaryKeyTableConstraint}
	 * labeled alternative in {@link SpeakQlParser#tableConstraint}.
	 * @param ctx the parse tree
	 */
	void exitPrimaryKeyTableConstraint(SpeakQlParser.PrimaryKeyTableConstraintContext ctx);
	/**
	 * Enter a parse tree produced by the {@code uniqueKeyTableConstraint}
	 * labeled alternative in {@link SpeakQlParser#tableConstraint}.
	 * @param ctx the parse tree
	 */
	void enterUniqueKeyTableConstraint(SpeakQlParser.UniqueKeyTableConstraintContext ctx);
	/**
	 * Exit a parse tree produced by the {@code uniqueKeyTableConstraint}
	 * labeled alternative in {@link SpeakQlParser#tableConstraint}.
	 * @param ctx the parse tree
	 */
	void exitUniqueKeyTableConstraint(SpeakQlParser.UniqueKeyTableConstraintContext ctx);
	/**
	 * Enter a parse tree produced by the {@code foreignKeyTableConstraint}
	 * labeled alternative in {@link SpeakQlParser#tableConstraint}.
	 * @param ctx the parse tree
	 */
	void enterForeignKeyTableConstraint(SpeakQlParser.ForeignKeyTableConstraintContext ctx);
	/**
	 * Exit a parse tree produced by the {@code foreignKeyTableConstraint}
	 * labeled alternative in {@link SpeakQlParser#tableConstraint}.
	 * @param ctx the parse tree
	 */
	void exitForeignKeyTableConstraint(SpeakQlParser.ForeignKeyTableConstraintContext ctx);
	/**
	 * Enter a parse tree produced by the {@code checkTableConstraint}
	 * labeled alternative in {@link SpeakQlParser#tableConstraint}.
	 * @param ctx the parse tree
	 */
	void enterCheckTableConstraint(SpeakQlParser.CheckTableConstraintContext ctx);
	/**
	 * Exit a parse tree produced by the {@code checkTableConstraint}
	 * labeled alternative in {@link SpeakQlParser#tableConstraint}.
	 * @param ctx the parse tree
	 */
	void exitCheckTableConstraint(SpeakQlParser.CheckTableConstraintContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#referenceDefinition}.
	 * @param ctx the parse tree
	 */
	void enterReferenceDefinition(SpeakQlParser.ReferenceDefinitionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#referenceDefinition}.
	 * @param ctx the parse tree
	 */
	void exitReferenceDefinition(SpeakQlParser.ReferenceDefinitionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#referenceAction}.
	 * @param ctx the parse tree
	 */
	void enterReferenceAction(SpeakQlParser.ReferenceActionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#referenceAction}.
	 * @param ctx the parse tree
	 */
	void exitReferenceAction(SpeakQlParser.ReferenceActionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#referenceControlType}.
	 * @param ctx the parse tree
	 */
	void enterReferenceControlType(SpeakQlParser.ReferenceControlTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#referenceControlType}.
	 * @param ctx the parse tree
	 */
	void exitReferenceControlType(SpeakQlParser.ReferenceControlTypeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code simpleIndexDeclaration}
	 * labeled alternative in {@link SpeakQlParser#indexColumnDefinition}.
	 * @param ctx the parse tree
	 */
	void enterSimpleIndexDeclaration(SpeakQlParser.SimpleIndexDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by the {@code simpleIndexDeclaration}
	 * labeled alternative in {@link SpeakQlParser#indexColumnDefinition}.
	 * @param ctx the parse tree
	 */
	void exitSimpleIndexDeclaration(SpeakQlParser.SimpleIndexDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code specialIndexDeclaration}
	 * labeled alternative in {@link SpeakQlParser#indexColumnDefinition}.
	 * @param ctx the parse tree
	 */
	void enterSpecialIndexDeclaration(SpeakQlParser.SpecialIndexDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by the {@code specialIndexDeclaration}
	 * labeled alternative in {@link SpeakQlParser#indexColumnDefinition}.
	 * @param ctx the parse tree
	 */
	void exitSpecialIndexDeclaration(SpeakQlParser.SpecialIndexDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tableOptionEngine}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void enterTableOptionEngine(SpeakQlParser.TableOptionEngineContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tableOptionEngine}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void exitTableOptionEngine(SpeakQlParser.TableOptionEngineContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tableOptionAutoIncrement}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void enterTableOptionAutoIncrement(SpeakQlParser.TableOptionAutoIncrementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tableOptionAutoIncrement}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void exitTableOptionAutoIncrement(SpeakQlParser.TableOptionAutoIncrementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tableOptionAverage}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void enterTableOptionAverage(SpeakQlParser.TableOptionAverageContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tableOptionAverage}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void exitTableOptionAverage(SpeakQlParser.TableOptionAverageContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tableOptionCharset}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void enterTableOptionCharset(SpeakQlParser.TableOptionCharsetContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tableOptionCharset}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void exitTableOptionCharset(SpeakQlParser.TableOptionCharsetContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tableOptionChecksum}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void enterTableOptionChecksum(SpeakQlParser.TableOptionChecksumContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tableOptionChecksum}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void exitTableOptionChecksum(SpeakQlParser.TableOptionChecksumContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tableOptionCollate}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void enterTableOptionCollate(SpeakQlParser.TableOptionCollateContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tableOptionCollate}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void exitTableOptionCollate(SpeakQlParser.TableOptionCollateContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tableOptionComment}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void enterTableOptionComment(SpeakQlParser.TableOptionCommentContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tableOptionComment}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void exitTableOptionComment(SpeakQlParser.TableOptionCommentContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tableOptionCompression}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void enterTableOptionCompression(SpeakQlParser.TableOptionCompressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tableOptionCompression}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void exitTableOptionCompression(SpeakQlParser.TableOptionCompressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tableOptionConnection}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void enterTableOptionConnection(SpeakQlParser.TableOptionConnectionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tableOptionConnection}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void exitTableOptionConnection(SpeakQlParser.TableOptionConnectionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tableOptionDataDirectory}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void enterTableOptionDataDirectory(SpeakQlParser.TableOptionDataDirectoryContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tableOptionDataDirectory}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void exitTableOptionDataDirectory(SpeakQlParser.TableOptionDataDirectoryContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tableOptionDelay}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void enterTableOptionDelay(SpeakQlParser.TableOptionDelayContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tableOptionDelay}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void exitTableOptionDelay(SpeakQlParser.TableOptionDelayContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tableOptionEncryption}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void enterTableOptionEncryption(SpeakQlParser.TableOptionEncryptionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tableOptionEncryption}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void exitTableOptionEncryption(SpeakQlParser.TableOptionEncryptionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tableOptionIndexDirectory}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void enterTableOptionIndexDirectory(SpeakQlParser.TableOptionIndexDirectoryContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tableOptionIndexDirectory}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void exitTableOptionIndexDirectory(SpeakQlParser.TableOptionIndexDirectoryContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tableOptionInsertMethod}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void enterTableOptionInsertMethod(SpeakQlParser.TableOptionInsertMethodContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tableOptionInsertMethod}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void exitTableOptionInsertMethod(SpeakQlParser.TableOptionInsertMethodContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tableOptionKeyBlockSize}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void enterTableOptionKeyBlockSize(SpeakQlParser.TableOptionKeyBlockSizeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tableOptionKeyBlockSize}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void exitTableOptionKeyBlockSize(SpeakQlParser.TableOptionKeyBlockSizeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tableOptionMaxRows}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void enterTableOptionMaxRows(SpeakQlParser.TableOptionMaxRowsContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tableOptionMaxRows}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void exitTableOptionMaxRows(SpeakQlParser.TableOptionMaxRowsContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tableOptionMinRows}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void enterTableOptionMinRows(SpeakQlParser.TableOptionMinRowsContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tableOptionMinRows}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void exitTableOptionMinRows(SpeakQlParser.TableOptionMinRowsContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tableOptionPackKeys}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void enterTableOptionPackKeys(SpeakQlParser.TableOptionPackKeysContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tableOptionPackKeys}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void exitTableOptionPackKeys(SpeakQlParser.TableOptionPackKeysContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tableOptionPassword}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void enterTableOptionPassword(SpeakQlParser.TableOptionPasswordContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tableOptionPassword}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void exitTableOptionPassword(SpeakQlParser.TableOptionPasswordContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tableOptionRowFormat}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void enterTableOptionRowFormat(SpeakQlParser.TableOptionRowFormatContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tableOptionRowFormat}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void exitTableOptionRowFormat(SpeakQlParser.TableOptionRowFormatContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tableOptionRecalculation}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void enterTableOptionRecalculation(SpeakQlParser.TableOptionRecalculationContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tableOptionRecalculation}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void exitTableOptionRecalculation(SpeakQlParser.TableOptionRecalculationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tableOptionPersistent}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void enterTableOptionPersistent(SpeakQlParser.TableOptionPersistentContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tableOptionPersistent}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void exitTableOptionPersistent(SpeakQlParser.TableOptionPersistentContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tableOptionSamplePage}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void enterTableOptionSamplePage(SpeakQlParser.TableOptionSamplePageContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tableOptionSamplePage}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void exitTableOptionSamplePage(SpeakQlParser.TableOptionSamplePageContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tableOptionTablespace}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void enterTableOptionTablespace(SpeakQlParser.TableOptionTablespaceContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tableOptionTablespace}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void exitTableOptionTablespace(SpeakQlParser.TableOptionTablespaceContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tableOptionTableType}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void enterTableOptionTableType(SpeakQlParser.TableOptionTableTypeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tableOptionTableType}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void exitTableOptionTableType(SpeakQlParser.TableOptionTableTypeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tableOptionUnion}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void enterTableOptionUnion(SpeakQlParser.TableOptionUnionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tableOptionUnion}
	 * labeled alternative in {@link SpeakQlParser#tableOption}.
	 * @param ctx the parse tree
	 */
	void exitTableOptionUnion(SpeakQlParser.TableOptionUnionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#tableType}.
	 * @param ctx the parse tree
	 */
	void enterTableType(SpeakQlParser.TableTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#tableType}.
	 * @param ctx the parse tree
	 */
	void exitTableType(SpeakQlParser.TableTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#tablespaceStorage}.
	 * @param ctx the parse tree
	 */
	void enterTablespaceStorage(SpeakQlParser.TablespaceStorageContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#tablespaceStorage}.
	 * @param ctx the parse tree
	 */
	void exitTablespaceStorage(SpeakQlParser.TablespaceStorageContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#partitionDefinitions}.
	 * @param ctx the parse tree
	 */
	void enterPartitionDefinitions(SpeakQlParser.PartitionDefinitionsContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#partitionDefinitions}.
	 * @param ctx the parse tree
	 */
	void exitPartitionDefinitions(SpeakQlParser.PartitionDefinitionsContext ctx);
	/**
	 * Enter a parse tree produced by the {@code partitionFunctionHash}
	 * labeled alternative in {@link SpeakQlParser#partitionFunctionDefinition}.
	 * @param ctx the parse tree
	 */
	void enterPartitionFunctionHash(SpeakQlParser.PartitionFunctionHashContext ctx);
	/**
	 * Exit a parse tree produced by the {@code partitionFunctionHash}
	 * labeled alternative in {@link SpeakQlParser#partitionFunctionDefinition}.
	 * @param ctx the parse tree
	 */
	void exitPartitionFunctionHash(SpeakQlParser.PartitionFunctionHashContext ctx);
	/**
	 * Enter a parse tree produced by the {@code partitionFunctionKey}
	 * labeled alternative in {@link SpeakQlParser#partitionFunctionDefinition}.
	 * @param ctx the parse tree
	 */
	void enterPartitionFunctionKey(SpeakQlParser.PartitionFunctionKeyContext ctx);
	/**
	 * Exit a parse tree produced by the {@code partitionFunctionKey}
	 * labeled alternative in {@link SpeakQlParser#partitionFunctionDefinition}.
	 * @param ctx the parse tree
	 */
	void exitPartitionFunctionKey(SpeakQlParser.PartitionFunctionKeyContext ctx);
	/**
	 * Enter a parse tree produced by the {@code partitionFunctionRange}
	 * labeled alternative in {@link SpeakQlParser#partitionFunctionDefinition}.
	 * @param ctx the parse tree
	 */
	void enterPartitionFunctionRange(SpeakQlParser.PartitionFunctionRangeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code partitionFunctionRange}
	 * labeled alternative in {@link SpeakQlParser#partitionFunctionDefinition}.
	 * @param ctx the parse tree
	 */
	void exitPartitionFunctionRange(SpeakQlParser.PartitionFunctionRangeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code partitionFunctionList}
	 * labeled alternative in {@link SpeakQlParser#partitionFunctionDefinition}.
	 * @param ctx the parse tree
	 */
	void enterPartitionFunctionList(SpeakQlParser.PartitionFunctionListContext ctx);
	/**
	 * Exit a parse tree produced by the {@code partitionFunctionList}
	 * labeled alternative in {@link SpeakQlParser#partitionFunctionDefinition}.
	 * @param ctx the parse tree
	 */
	void exitPartitionFunctionList(SpeakQlParser.PartitionFunctionListContext ctx);
	/**
	 * Enter a parse tree produced by the {@code subPartitionFunctionHash}
	 * labeled alternative in {@link SpeakQlParser#subpartitionFunctionDefinition}.
	 * @param ctx the parse tree
	 */
	void enterSubPartitionFunctionHash(SpeakQlParser.SubPartitionFunctionHashContext ctx);
	/**
	 * Exit a parse tree produced by the {@code subPartitionFunctionHash}
	 * labeled alternative in {@link SpeakQlParser#subpartitionFunctionDefinition}.
	 * @param ctx the parse tree
	 */
	void exitSubPartitionFunctionHash(SpeakQlParser.SubPartitionFunctionHashContext ctx);
	/**
	 * Enter a parse tree produced by the {@code subPartitionFunctionKey}
	 * labeled alternative in {@link SpeakQlParser#subpartitionFunctionDefinition}.
	 * @param ctx the parse tree
	 */
	void enterSubPartitionFunctionKey(SpeakQlParser.SubPartitionFunctionKeyContext ctx);
	/**
	 * Exit a parse tree produced by the {@code subPartitionFunctionKey}
	 * labeled alternative in {@link SpeakQlParser#subpartitionFunctionDefinition}.
	 * @param ctx the parse tree
	 */
	void exitSubPartitionFunctionKey(SpeakQlParser.SubPartitionFunctionKeyContext ctx);
	/**
	 * Enter a parse tree produced by the {@code partitionComparison}
	 * labeled alternative in {@link SpeakQlParser#partitionDefinition}.
	 * @param ctx the parse tree
	 */
	void enterPartitionComparison(SpeakQlParser.PartitionComparisonContext ctx);
	/**
	 * Exit a parse tree produced by the {@code partitionComparison}
	 * labeled alternative in {@link SpeakQlParser#partitionDefinition}.
	 * @param ctx the parse tree
	 */
	void exitPartitionComparison(SpeakQlParser.PartitionComparisonContext ctx);
	/**
	 * Enter a parse tree produced by the {@code partitionListAtom}
	 * labeled alternative in {@link SpeakQlParser#partitionDefinition}.
	 * @param ctx the parse tree
	 */
	void enterPartitionListAtom(SpeakQlParser.PartitionListAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code partitionListAtom}
	 * labeled alternative in {@link SpeakQlParser#partitionDefinition}.
	 * @param ctx the parse tree
	 */
	void exitPartitionListAtom(SpeakQlParser.PartitionListAtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code partitionListVector}
	 * labeled alternative in {@link SpeakQlParser#partitionDefinition}.
	 * @param ctx the parse tree
	 */
	void enterPartitionListVector(SpeakQlParser.PartitionListVectorContext ctx);
	/**
	 * Exit a parse tree produced by the {@code partitionListVector}
	 * labeled alternative in {@link SpeakQlParser#partitionDefinition}.
	 * @param ctx the parse tree
	 */
	void exitPartitionListVector(SpeakQlParser.PartitionListVectorContext ctx);
	/**
	 * Enter a parse tree produced by the {@code partitionSimple}
	 * labeled alternative in {@link SpeakQlParser#partitionDefinition}.
	 * @param ctx the parse tree
	 */
	void enterPartitionSimple(SpeakQlParser.PartitionSimpleContext ctx);
	/**
	 * Exit a parse tree produced by the {@code partitionSimple}
	 * labeled alternative in {@link SpeakQlParser#partitionDefinition}.
	 * @param ctx the parse tree
	 */
	void exitPartitionSimple(SpeakQlParser.PartitionSimpleContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#partitionDefinerAtom}.
	 * @param ctx the parse tree
	 */
	void enterPartitionDefinerAtom(SpeakQlParser.PartitionDefinerAtomContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#partitionDefinerAtom}.
	 * @param ctx the parse tree
	 */
	void exitPartitionDefinerAtom(SpeakQlParser.PartitionDefinerAtomContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#partitionDefinerVector}.
	 * @param ctx the parse tree
	 */
	void enterPartitionDefinerVector(SpeakQlParser.PartitionDefinerVectorContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#partitionDefinerVector}.
	 * @param ctx the parse tree
	 */
	void exitPartitionDefinerVector(SpeakQlParser.PartitionDefinerVectorContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#subpartitionDefinition}.
	 * @param ctx the parse tree
	 */
	void enterSubpartitionDefinition(SpeakQlParser.SubpartitionDefinitionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#subpartitionDefinition}.
	 * @param ctx the parse tree
	 */
	void exitSubpartitionDefinition(SpeakQlParser.SubpartitionDefinitionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code partitionOptionEngine}
	 * labeled alternative in {@link SpeakQlParser#partitionOption}.
	 * @param ctx the parse tree
	 */
	void enterPartitionOptionEngine(SpeakQlParser.PartitionOptionEngineContext ctx);
	/**
	 * Exit a parse tree produced by the {@code partitionOptionEngine}
	 * labeled alternative in {@link SpeakQlParser#partitionOption}.
	 * @param ctx the parse tree
	 */
	void exitPartitionOptionEngine(SpeakQlParser.PartitionOptionEngineContext ctx);
	/**
	 * Enter a parse tree produced by the {@code partitionOptionComment}
	 * labeled alternative in {@link SpeakQlParser#partitionOption}.
	 * @param ctx the parse tree
	 */
	void enterPartitionOptionComment(SpeakQlParser.PartitionOptionCommentContext ctx);
	/**
	 * Exit a parse tree produced by the {@code partitionOptionComment}
	 * labeled alternative in {@link SpeakQlParser#partitionOption}.
	 * @param ctx the parse tree
	 */
	void exitPartitionOptionComment(SpeakQlParser.PartitionOptionCommentContext ctx);
	/**
	 * Enter a parse tree produced by the {@code partitionOptionDataDirectory}
	 * labeled alternative in {@link SpeakQlParser#partitionOption}.
	 * @param ctx the parse tree
	 */
	void enterPartitionOptionDataDirectory(SpeakQlParser.PartitionOptionDataDirectoryContext ctx);
	/**
	 * Exit a parse tree produced by the {@code partitionOptionDataDirectory}
	 * labeled alternative in {@link SpeakQlParser#partitionOption}.
	 * @param ctx the parse tree
	 */
	void exitPartitionOptionDataDirectory(SpeakQlParser.PartitionOptionDataDirectoryContext ctx);
	/**
	 * Enter a parse tree produced by the {@code partitionOptionIndexDirectory}
	 * labeled alternative in {@link SpeakQlParser#partitionOption}.
	 * @param ctx the parse tree
	 */
	void enterPartitionOptionIndexDirectory(SpeakQlParser.PartitionOptionIndexDirectoryContext ctx);
	/**
	 * Exit a parse tree produced by the {@code partitionOptionIndexDirectory}
	 * labeled alternative in {@link SpeakQlParser#partitionOption}.
	 * @param ctx the parse tree
	 */
	void exitPartitionOptionIndexDirectory(SpeakQlParser.PartitionOptionIndexDirectoryContext ctx);
	/**
	 * Enter a parse tree produced by the {@code partitionOptionMaxRows}
	 * labeled alternative in {@link SpeakQlParser#partitionOption}.
	 * @param ctx the parse tree
	 */
	void enterPartitionOptionMaxRows(SpeakQlParser.PartitionOptionMaxRowsContext ctx);
	/**
	 * Exit a parse tree produced by the {@code partitionOptionMaxRows}
	 * labeled alternative in {@link SpeakQlParser#partitionOption}.
	 * @param ctx the parse tree
	 */
	void exitPartitionOptionMaxRows(SpeakQlParser.PartitionOptionMaxRowsContext ctx);
	/**
	 * Enter a parse tree produced by the {@code partitionOptionMinRows}
	 * labeled alternative in {@link SpeakQlParser#partitionOption}.
	 * @param ctx the parse tree
	 */
	void enterPartitionOptionMinRows(SpeakQlParser.PartitionOptionMinRowsContext ctx);
	/**
	 * Exit a parse tree produced by the {@code partitionOptionMinRows}
	 * labeled alternative in {@link SpeakQlParser#partitionOption}.
	 * @param ctx the parse tree
	 */
	void exitPartitionOptionMinRows(SpeakQlParser.PartitionOptionMinRowsContext ctx);
	/**
	 * Enter a parse tree produced by the {@code partitionOptionTablespace}
	 * labeled alternative in {@link SpeakQlParser#partitionOption}.
	 * @param ctx the parse tree
	 */
	void enterPartitionOptionTablespace(SpeakQlParser.PartitionOptionTablespaceContext ctx);
	/**
	 * Exit a parse tree produced by the {@code partitionOptionTablespace}
	 * labeled alternative in {@link SpeakQlParser#partitionOption}.
	 * @param ctx the parse tree
	 */
	void exitPartitionOptionTablespace(SpeakQlParser.PartitionOptionTablespaceContext ctx);
	/**
	 * Enter a parse tree produced by the {@code partitionOptionNodeGroup}
	 * labeled alternative in {@link SpeakQlParser#partitionOption}.
	 * @param ctx the parse tree
	 */
	void enterPartitionOptionNodeGroup(SpeakQlParser.PartitionOptionNodeGroupContext ctx);
	/**
	 * Exit a parse tree produced by the {@code partitionOptionNodeGroup}
	 * labeled alternative in {@link SpeakQlParser#partitionOption}.
	 * @param ctx the parse tree
	 */
	void exitPartitionOptionNodeGroup(SpeakQlParser.PartitionOptionNodeGroupContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterSimpleDatabase}
	 * labeled alternative in {@link SpeakQlParser#alterDatabase}.
	 * @param ctx the parse tree
	 */
	void enterAlterSimpleDatabase(SpeakQlParser.AlterSimpleDatabaseContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterSimpleDatabase}
	 * labeled alternative in {@link SpeakQlParser#alterDatabase}.
	 * @param ctx the parse tree
	 */
	void exitAlterSimpleDatabase(SpeakQlParser.AlterSimpleDatabaseContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterUpgradeName}
	 * labeled alternative in {@link SpeakQlParser#alterDatabase}.
	 * @param ctx the parse tree
	 */
	void enterAlterUpgradeName(SpeakQlParser.AlterUpgradeNameContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterUpgradeName}
	 * labeled alternative in {@link SpeakQlParser#alterDatabase}.
	 * @param ctx the parse tree
	 */
	void exitAlterUpgradeName(SpeakQlParser.AlterUpgradeNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#alterEvent}.
	 * @param ctx the parse tree
	 */
	void enterAlterEvent(SpeakQlParser.AlterEventContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#alterEvent}.
	 * @param ctx the parse tree
	 */
	void exitAlterEvent(SpeakQlParser.AlterEventContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#alterFunction}.
	 * @param ctx the parse tree
	 */
	void enterAlterFunction(SpeakQlParser.AlterFunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#alterFunction}.
	 * @param ctx the parse tree
	 */
	void exitAlterFunction(SpeakQlParser.AlterFunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#alterInstance}.
	 * @param ctx the parse tree
	 */
	void enterAlterInstance(SpeakQlParser.AlterInstanceContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#alterInstance}.
	 * @param ctx the parse tree
	 */
	void exitAlterInstance(SpeakQlParser.AlterInstanceContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#alterLogfileGroup}.
	 * @param ctx the parse tree
	 */
	void enterAlterLogfileGroup(SpeakQlParser.AlterLogfileGroupContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#alterLogfileGroup}.
	 * @param ctx the parse tree
	 */
	void exitAlterLogfileGroup(SpeakQlParser.AlterLogfileGroupContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#alterProcedure}.
	 * @param ctx the parse tree
	 */
	void enterAlterProcedure(SpeakQlParser.AlterProcedureContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#alterProcedure}.
	 * @param ctx the parse tree
	 */
	void exitAlterProcedure(SpeakQlParser.AlterProcedureContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#alterServer}.
	 * @param ctx the parse tree
	 */
	void enterAlterServer(SpeakQlParser.AlterServerContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#alterServer}.
	 * @param ctx the parse tree
	 */
	void exitAlterServer(SpeakQlParser.AlterServerContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#alterTable}.
	 * @param ctx the parse tree
	 */
	void enterAlterTable(SpeakQlParser.AlterTableContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#alterTable}.
	 * @param ctx the parse tree
	 */
	void exitAlterTable(SpeakQlParser.AlterTableContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#alterTablespace}.
	 * @param ctx the parse tree
	 */
	void enterAlterTablespace(SpeakQlParser.AlterTablespaceContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#alterTablespace}.
	 * @param ctx the parse tree
	 */
	void exitAlterTablespace(SpeakQlParser.AlterTablespaceContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#alterView}.
	 * @param ctx the parse tree
	 */
	void enterAlterView(SpeakQlParser.AlterViewContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#alterView}.
	 * @param ctx the parse tree
	 */
	void exitAlterView(SpeakQlParser.AlterViewContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByTableOption}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByTableOption(SpeakQlParser.AlterByTableOptionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByTableOption}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByTableOption(SpeakQlParser.AlterByTableOptionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByAddColumn}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByAddColumn(SpeakQlParser.AlterByAddColumnContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByAddColumn}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByAddColumn(SpeakQlParser.AlterByAddColumnContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByAddColumns}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByAddColumns(SpeakQlParser.AlterByAddColumnsContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByAddColumns}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByAddColumns(SpeakQlParser.AlterByAddColumnsContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByAddIndex}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByAddIndex(SpeakQlParser.AlterByAddIndexContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByAddIndex}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByAddIndex(SpeakQlParser.AlterByAddIndexContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByAddPrimaryKey}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByAddPrimaryKey(SpeakQlParser.AlterByAddPrimaryKeyContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByAddPrimaryKey}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByAddPrimaryKey(SpeakQlParser.AlterByAddPrimaryKeyContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByAddUniqueKey}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByAddUniqueKey(SpeakQlParser.AlterByAddUniqueKeyContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByAddUniqueKey}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByAddUniqueKey(SpeakQlParser.AlterByAddUniqueKeyContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByAddSpecialIndex}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByAddSpecialIndex(SpeakQlParser.AlterByAddSpecialIndexContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByAddSpecialIndex}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByAddSpecialIndex(SpeakQlParser.AlterByAddSpecialIndexContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByAddForeignKey}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByAddForeignKey(SpeakQlParser.AlterByAddForeignKeyContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByAddForeignKey}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByAddForeignKey(SpeakQlParser.AlterByAddForeignKeyContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByAddCheckTableConstraint}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByAddCheckTableConstraint(SpeakQlParser.AlterByAddCheckTableConstraintContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByAddCheckTableConstraint}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByAddCheckTableConstraint(SpeakQlParser.AlterByAddCheckTableConstraintContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterBySetAlgorithm}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterBySetAlgorithm(SpeakQlParser.AlterBySetAlgorithmContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterBySetAlgorithm}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterBySetAlgorithm(SpeakQlParser.AlterBySetAlgorithmContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByChangeDefault}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByChangeDefault(SpeakQlParser.AlterByChangeDefaultContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByChangeDefault}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByChangeDefault(SpeakQlParser.AlterByChangeDefaultContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByChangeColumn}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByChangeColumn(SpeakQlParser.AlterByChangeColumnContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByChangeColumn}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByChangeColumn(SpeakQlParser.AlterByChangeColumnContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByRenameColumn}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByRenameColumn(SpeakQlParser.AlterByRenameColumnContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByRenameColumn}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByRenameColumn(SpeakQlParser.AlterByRenameColumnContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByLock}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByLock(SpeakQlParser.AlterByLockContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByLock}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByLock(SpeakQlParser.AlterByLockContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByModifyColumn}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByModifyColumn(SpeakQlParser.AlterByModifyColumnContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByModifyColumn}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByModifyColumn(SpeakQlParser.AlterByModifyColumnContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByDropColumn}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByDropColumn(SpeakQlParser.AlterByDropColumnContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByDropColumn}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByDropColumn(SpeakQlParser.AlterByDropColumnContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByDropConstraintCheck}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByDropConstraintCheck(SpeakQlParser.AlterByDropConstraintCheckContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByDropConstraintCheck}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByDropConstraintCheck(SpeakQlParser.AlterByDropConstraintCheckContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByDropPrimaryKey}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByDropPrimaryKey(SpeakQlParser.AlterByDropPrimaryKeyContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByDropPrimaryKey}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByDropPrimaryKey(SpeakQlParser.AlterByDropPrimaryKeyContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByRenameIndex}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByRenameIndex(SpeakQlParser.AlterByRenameIndexContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByRenameIndex}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByRenameIndex(SpeakQlParser.AlterByRenameIndexContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByAlterIndexVisibility}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByAlterIndexVisibility(SpeakQlParser.AlterByAlterIndexVisibilityContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByAlterIndexVisibility}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByAlterIndexVisibility(SpeakQlParser.AlterByAlterIndexVisibilityContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByDropIndex}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByDropIndex(SpeakQlParser.AlterByDropIndexContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByDropIndex}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByDropIndex(SpeakQlParser.AlterByDropIndexContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByDropForeignKey}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByDropForeignKey(SpeakQlParser.AlterByDropForeignKeyContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByDropForeignKey}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByDropForeignKey(SpeakQlParser.AlterByDropForeignKeyContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByDisableKeys}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByDisableKeys(SpeakQlParser.AlterByDisableKeysContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByDisableKeys}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByDisableKeys(SpeakQlParser.AlterByDisableKeysContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByEnableKeys}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByEnableKeys(SpeakQlParser.AlterByEnableKeysContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByEnableKeys}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByEnableKeys(SpeakQlParser.AlterByEnableKeysContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByRename}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByRename(SpeakQlParser.AlterByRenameContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByRename}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByRename(SpeakQlParser.AlterByRenameContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByOrder}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByOrder(SpeakQlParser.AlterByOrderContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByOrder}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByOrder(SpeakQlParser.AlterByOrderContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByConvertCharset}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByConvertCharset(SpeakQlParser.AlterByConvertCharsetContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByConvertCharset}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByConvertCharset(SpeakQlParser.AlterByConvertCharsetContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByDefaultCharset}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByDefaultCharset(SpeakQlParser.AlterByDefaultCharsetContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByDefaultCharset}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByDefaultCharset(SpeakQlParser.AlterByDefaultCharsetContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByDiscardTablespace}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByDiscardTablespace(SpeakQlParser.AlterByDiscardTablespaceContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByDiscardTablespace}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByDiscardTablespace(SpeakQlParser.AlterByDiscardTablespaceContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByImportTablespace}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByImportTablespace(SpeakQlParser.AlterByImportTablespaceContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByImportTablespace}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByImportTablespace(SpeakQlParser.AlterByImportTablespaceContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByForce}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByForce(SpeakQlParser.AlterByForceContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByForce}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByForce(SpeakQlParser.AlterByForceContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByValidate}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByValidate(SpeakQlParser.AlterByValidateContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByValidate}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByValidate(SpeakQlParser.AlterByValidateContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByAddPartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByAddPartition(SpeakQlParser.AlterByAddPartitionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByAddPartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByAddPartition(SpeakQlParser.AlterByAddPartitionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByDropPartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByDropPartition(SpeakQlParser.AlterByDropPartitionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByDropPartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByDropPartition(SpeakQlParser.AlterByDropPartitionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByDiscardPartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByDiscardPartition(SpeakQlParser.AlterByDiscardPartitionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByDiscardPartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByDiscardPartition(SpeakQlParser.AlterByDiscardPartitionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByImportPartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByImportPartition(SpeakQlParser.AlterByImportPartitionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByImportPartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByImportPartition(SpeakQlParser.AlterByImportPartitionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByTruncatePartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByTruncatePartition(SpeakQlParser.AlterByTruncatePartitionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByTruncatePartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByTruncatePartition(SpeakQlParser.AlterByTruncatePartitionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByCoalescePartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByCoalescePartition(SpeakQlParser.AlterByCoalescePartitionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByCoalescePartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByCoalescePartition(SpeakQlParser.AlterByCoalescePartitionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByReorganizePartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByReorganizePartition(SpeakQlParser.AlterByReorganizePartitionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByReorganizePartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByReorganizePartition(SpeakQlParser.AlterByReorganizePartitionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByExchangePartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByExchangePartition(SpeakQlParser.AlterByExchangePartitionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByExchangePartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByExchangePartition(SpeakQlParser.AlterByExchangePartitionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByAnalyzePartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByAnalyzePartition(SpeakQlParser.AlterByAnalyzePartitionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByAnalyzePartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByAnalyzePartition(SpeakQlParser.AlterByAnalyzePartitionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByCheckPartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByCheckPartition(SpeakQlParser.AlterByCheckPartitionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByCheckPartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByCheckPartition(SpeakQlParser.AlterByCheckPartitionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByOptimizePartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByOptimizePartition(SpeakQlParser.AlterByOptimizePartitionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByOptimizePartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByOptimizePartition(SpeakQlParser.AlterByOptimizePartitionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByRebuildPartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByRebuildPartition(SpeakQlParser.AlterByRebuildPartitionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByRebuildPartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByRebuildPartition(SpeakQlParser.AlterByRebuildPartitionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByRepairPartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByRepairPartition(SpeakQlParser.AlterByRepairPartitionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByRepairPartition}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByRepairPartition(SpeakQlParser.AlterByRepairPartitionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByRemovePartitioning}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByRemovePartitioning(SpeakQlParser.AlterByRemovePartitioningContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByRemovePartitioning}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByRemovePartitioning(SpeakQlParser.AlterByRemovePartitioningContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterByUpgradePartitioning}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void enterAlterByUpgradePartitioning(SpeakQlParser.AlterByUpgradePartitioningContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alterByUpgradePartitioning}
	 * labeled alternative in {@link SpeakQlParser#alterSpecification}.
	 * @param ctx the parse tree
	 */
	void exitAlterByUpgradePartitioning(SpeakQlParser.AlterByUpgradePartitioningContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#dropDatabase}.
	 * @param ctx the parse tree
	 */
	void enterDropDatabase(SpeakQlParser.DropDatabaseContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#dropDatabase}.
	 * @param ctx the parse tree
	 */
	void exitDropDatabase(SpeakQlParser.DropDatabaseContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#dropEvent}.
	 * @param ctx the parse tree
	 */
	void enterDropEvent(SpeakQlParser.DropEventContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#dropEvent}.
	 * @param ctx the parse tree
	 */
	void exitDropEvent(SpeakQlParser.DropEventContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#dropIndex}.
	 * @param ctx the parse tree
	 */
	void enterDropIndex(SpeakQlParser.DropIndexContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#dropIndex}.
	 * @param ctx the parse tree
	 */
	void exitDropIndex(SpeakQlParser.DropIndexContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#dropLogfileGroup}.
	 * @param ctx the parse tree
	 */
	void enterDropLogfileGroup(SpeakQlParser.DropLogfileGroupContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#dropLogfileGroup}.
	 * @param ctx the parse tree
	 */
	void exitDropLogfileGroup(SpeakQlParser.DropLogfileGroupContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#dropProcedure}.
	 * @param ctx the parse tree
	 */
	void enterDropProcedure(SpeakQlParser.DropProcedureContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#dropProcedure}.
	 * @param ctx the parse tree
	 */
	void exitDropProcedure(SpeakQlParser.DropProcedureContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#dropFunction}.
	 * @param ctx the parse tree
	 */
	void enterDropFunction(SpeakQlParser.DropFunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#dropFunction}.
	 * @param ctx the parse tree
	 */
	void exitDropFunction(SpeakQlParser.DropFunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#dropServer}.
	 * @param ctx the parse tree
	 */
	void enterDropServer(SpeakQlParser.DropServerContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#dropServer}.
	 * @param ctx the parse tree
	 */
	void exitDropServer(SpeakQlParser.DropServerContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#dropTable}.
	 * @param ctx the parse tree
	 */
	void enterDropTable(SpeakQlParser.DropTableContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#dropTable}.
	 * @param ctx the parse tree
	 */
	void exitDropTable(SpeakQlParser.DropTableContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#dropTablespace}.
	 * @param ctx the parse tree
	 */
	void enterDropTablespace(SpeakQlParser.DropTablespaceContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#dropTablespace}.
	 * @param ctx the parse tree
	 */
	void exitDropTablespace(SpeakQlParser.DropTablespaceContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#dropTrigger}.
	 * @param ctx the parse tree
	 */
	void enterDropTrigger(SpeakQlParser.DropTriggerContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#dropTrigger}.
	 * @param ctx the parse tree
	 */
	void exitDropTrigger(SpeakQlParser.DropTriggerContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#dropView}.
	 * @param ctx the parse tree
	 */
	void enterDropView(SpeakQlParser.DropViewContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#dropView}.
	 * @param ctx the parse tree
	 */
	void exitDropView(SpeakQlParser.DropViewContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#renameTable}.
	 * @param ctx the parse tree
	 */
	void enterRenameTable(SpeakQlParser.RenameTableContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#renameTable}.
	 * @param ctx the parse tree
	 */
	void exitRenameTable(SpeakQlParser.RenameTableContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#renameTableClause}.
	 * @param ctx the parse tree
	 */
	void enterRenameTableClause(SpeakQlParser.RenameTableClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#renameTableClause}.
	 * @param ctx the parse tree
	 */
	void exitRenameTableClause(SpeakQlParser.RenameTableClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#truncateTable}.
	 * @param ctx the parse tree
	 */
	void enterTruncateTable(SpeakQlParser.TruncateTableContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#truncateTable}.
	 * @param ctx the parse tree
	 */
	void exitTruncateTable(SpeakQlParser.TruncateTableContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#callStatement}.
	 * @param ctx the parse tree
	 */
	void enterCallStatement(SpeakQlParser.CallStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#callStatement}.
	 * @param ctx the parse tree
	 */
	void exitCallStatement(SpeakQlParser.CallStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#deleteStatement}.
	 * @param ctx the parse tree
	 */
	void enterDeleteStatement(SpeakQlParser.DeleteStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#deleteStatement}.
	 * @param ctx the parse tree
	 */
	void exitDeleteStatement(SpeakQlParser.DeleteStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#doStatement}.
	 * @param ctx the parse tree
	 */
	void enterDoStatement(SpeakQlParser.DoStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#doStatement}.
	 * @param ctx the parse tree
	 */
	void exitDoStatement(SpeakQlParser.DoStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#handlerStatement}.
	 * @param ctx the parse tree
	 */
	void enterHandlerStatement(SpeakQlParser.HandlerStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#handlerStatement}.
	 * @param ctx the parse tree
	 */
	void exitHandlerStatement(SpeakQlParser.HandlerStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#insertStatement}.
	 * @param ctx the parse tree
	 */
	void enterInsertStatement(SpeakQlParser.InsertStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#insertStatement}.
	 * @param ctx the parse tree
	 */
	void exitInsertStatement(SpeakQlParser.InsertStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#loadDataStatement}.
	 * @param ctx the parse tree
	 */
	void enterLoadDataStatement(SpeakQlParser.LoadDataStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#loadDataStatement}.
	 * @param ctx the parse tree
	 */
	void exitLoadDataStatement(SpeakQlParser.LoadDataStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#loadXmlStatement}.
	 * @param ctx the parse tree
	 */
	void enterLoadXmlStatement(SpeakQlParser.LoadXmlStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#loadXmlStatement}.
	 * @param ctx the parse tree
	 */
	void exitLoadXmlStatement(SpeakQlParser.LoadXmlStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#replaceStatement}.
	 * @param ctx the parse tree
	 */
	void enterReplaceStatement(SpeakQlParser.ReplaceStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#replaceStatement}.
	 * @param ctx the parse tree
	 */
	void exitReplaceStatement(SpeakQlParser.ReplaceStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code simpleSelect}
	 * labeled alternative in {@link SpeakQlParser#selectStatement}.
	 * @param ctx the parse tree
	 */
	void enterSimpleSelect(SpeakQlParser.SimpleSelectContext ctx);
	/**
	 * Exit a parse tree produced by the {@code simpleSelect}
	 * labeled alternative in {@link SpeakQlParser#selectStatement}.
	 * @param ctx the parse tree
	 */
	void exitSimpleSelect(SpeakQlParser.SimpleSelectContext ctx);
	/**
	 * Enter a parse tree produced by the {@code parenthesisSelect}
	 * labeled alternative in {@link SpeakQlParser#selectStatement}.
	 * @param ctx the parse tree
	 */
	void enterParenthesisSelect(SpeakQlParser.ParenthesisSelectContext ctx);
	/**
	 * Exit a parse tree produced by the {@code parenthesisSelect}
	 * labeled alternative in {@link SpeakQlParser#selectStatement}.
	 * @param ctx the parse tree
	 */
	void exitParenthesisSelect(SpeakQlParser.ParenthesisSelectContext ctx);
	/**
	 * Enter a parse tree produced by the {@code unionSelect}
	 * labeled alternative in {@link SpeakQlParser#selectStatement}.
	 * @param ctx the parse tree
	 */
	void enterUnionSelect(SpeakQlParser.UnionSelectContext ctx);
	/**
	 * Exit a parse tree produced by the {@code unionSelect}
	 * labeled alternative in {@link SpeakQlParser#selectStatement}.
	 * @param ctx the parse tree
	 */
	void exitUnionSelect(SpeakQlParser.UnionSelectContext ctx);
	/**
	 * Enter a parse tree produced by the {@code unionParenthesisSelect}
	 * labeled alternative in {@link SpeakQlParser#selectStatement}.
	 * @param ctx the parse tree
	 */
	void enterUnionParenthesisSelect(SpeakQlParser.UnionParenthesisSelectContext ctx);
	/**
	 * Exit a parse tree produced by the {@code unionParenthesisSelect}
	 * labeled alternative in {@link SpeakQlParser#selectStatement}.
	 * @param ctx the parse tree
	 */
	void exitUnionParenthesisSelect(SpeakQlParser.UnionParenthesisSelectContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#updateStatement}.
	 * @param ctx the parse tree
	 */
	void enterUpdateStatement(SpeakQlParser.UpdateStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#updateStatement}.
	 * @param ctx the parse tree
	 */
	void exitUpdateStatement(SpeakQlParser.UpdateStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#insertStatementValue}.
	 * @param ctx the parse tree
	 */
	void enterInsertStatementValue(SpeakQlParser.InsertStatementValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#insertStatementValue}.
	 * @param ctx the parse tree
	 */
	void exitInsertStatementValue(SpeakQlParser.InsertStatementValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#updatedElement}.
	 * @param ctx the parse tree
	 */
	void enterUpdatedElement(SpeakQlParser.UpdatedElementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#updatedElement}.
	 * @param ctx the parse tree
	 */
	void exitUpdatedElement(SpeakQlParser.UpdatedElementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#assignmentField}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentField(SpeakQlParser.AssignmentFieldContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#assignmentField}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentField(SpeakQlParser.AssignmentFieldContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#lockClause}.
	 * @param ctx the parse tree
	 */
	void enterLockClause(SpeakQlParser.LockClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#lockClause}.
	 * @param ctx the parse tree
	 */
	void exitLockClause(SpeakQlParser.LockClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#singleDeleteStatement}.
	 * @param ctx the parse tree
	 */
	void enterSingleDeleteStatement(SpeakQlParser.SingleDeleteStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#singleDeleteStatement}.
	 * @param ctx the parse tree
	 */
	void exitSingleDeleteStatement(SpeakQlParser.SingleDeleteStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#multipleDeleteStatement}.
	 * @param ctx the parse tree
	 */
	void enterMultipleDeleteStatement(SpeakQlParser.MultipleDeleteStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#multipleDeleteStatement}.
	 * @param ctx the parse tree
	 */
	void exitMultipleDeleteStatement(SpeakQlParser.MultipleDeleteStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#handlerOpenStatement}.
	 * @param ctx the parse tree
	 */
	void enterHandlerOpenStatement(SpeakQlParser.HandlerOpenStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#handlerOpenStatement}.
	 * @param ctx the parse tree
	 */
	void exitHandlerOpenStatement(SpeakQlParser.HandlerOpenStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#handlerReadIndexStatement}.
	 * @param ctx the parse tree
	 */
	void enterHandlerReadIndexStatement(SpeakQlParser.HandlerReadIndexStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#handlerReadIndexStatement}.
	 * @param ctx the parse tree
	 */
	void exitHandlerReadIndexStatement(SpeakQlParser.HandlerReadIndexStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#handlerReadStatement}.
	 * @param ctx the parse tree
	 */
	void enterHandlerReadStatement(SpeakQlParser.HandlerReadStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#handlerReadStatement}.
	 * @param ctx the parse tree
	 */
	void exitHandlerReadStatement(SpeakQlParser.HandlerReadStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#handlerCloseStatement}.
	 * @param ctx the parse tree
	 */
	void enterHandlerCloseStatement(SpeakQlParser.HandlerCloseStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#handlerCloseStatement}.
	 * @param ctx the parse tree
	 */
	void exitHandlerCloseStatement(SpeakQlParser.HandlerCloseStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#singleUpdateStatement}.
	 * @param ctx the parse tree
	 */
	void enterSingleUpdateStatement(SpeakQlParser.SingleUpdateStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#singleUpdateStatement}.
	 * @param ctx the parse tree
	 */
	void exitSingleUpdateStatement(SpeakQlParser.SingleUpdateStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#multipleUpdateStatement}.
	 * @param ctx the parse tree
	 */
	void enterMultipleUpdateStatement(SpeakQlParser.MultipleUpdateStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#multipleUpdateStatement}.
	 * @param ctx the parse tree
	 */
	void exitMultipleUpdateStatement(SpeakQlParser.MultipleUpdateStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#orderByClause}.
	 * @param ctx the parse tree
	 */
	void enterOrderByClause(SpeakQlParser.OrderByClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#orderByClause}.
	 * @param ctx the parse tree
	 */
	void exitOrderByClause(SpeakQlParser.OrderByClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#orderByExpression}.
	 * @param ctx the parse tree
	 */
	void enterOrderByExpression(SpeakQlParser.OrderByExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#orderByExpression}.
	 * @param ctx the parse tree
	 */
	void exitOrderByExpression(SpeakQlParser.OrderByExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#tableSources}.
	 * @param ctx the parse tree
	 */
	void enterTableSources(SpeakQlParser.TableSourcesContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#tableSources}.
	 * @param ctx the parse tree
	 */
	void exitTableSources(SpeakQlParser.TableSourcesContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tableSourceBase}
	 * labeled alternative in {@link SpeakQlParser#tableSource}.
	 * @param ctx the parse tree
	 */
	void enterTableSourceBase(SpeakQlParser.TableSourceBaseContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tableSourceBase}
	 * labeled alternative in {@link SpeakQlParser#tableSource}.
	 * @param ctx the parse tree
	 */
	void exitTableSourceBase(SpeakQlParser.TableSourceBaseContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tableSourceNested}
	 * labeled alternative in {@link SpeakQlParser#tableSource}.
	 * @param ctx the parse tree
	 */
	void enterTableSourceNested(SpeakQlParser.TableSourceNestedContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tableSourceNested}
	 * labeled alternative in {@link SpeakQlParser#tableSource}.
	 * @param ctx the parse tree
	 */
	void exitTableSourceNested(SpeakQlParser.TableSourceNestedContext ctx);
	/**
	 * Enter a parse tree produced by the {@code atomTableItem}
	 * labeled alternative in {@link SpeakQlParser#tableSourceItem}.
	 * @param ctx the parse tree
	 */
	void enterAtomTableItem(SpeakQlParser.AtomTableItemContext ctx);
	/**
	 * Exit a parse tree produced by the {@code atomTableItem}
	 * labeled alternative in {@link SpeakQlParser#tableSourceItem}.
	 * @param ctx the parse tree
	 */
	void exitAtomTableItem(SpeakQlParser.AtomTableItemContext ctx);
	/**
	 * Enter a parse tree produced by the {@code subqueryTableItem}
	 * labeled alternative in {@link SpeakQlParser#tableSourceItem}.
	 * @param ctx the parse tree
	 */
	void enterSubqueryTableItem(SpeakQlParser.SubqueryTableItemContext ctx);
	/**
	 * Exit a parse tree produced by the {@code subqueryTableItem}
	 * labeled alternative in {@link SpeakQlParser#tableSourceItem}.
	 * @param ctx the parse tree
	 */
	void exitSubqueryTableItem(SpeakQlParser.SubqueryTableItemContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tableSourcesItem}
	 * labeled alternative in {@link SpeakQlParser#tableSourceItem}.
	 * @param ctx the parse tree
	 */
	void enterTableSourcesItem(SpeakQlParser.TableSourcesItemContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tableSourcesItem}
	 * labeled alternative in {@link SpeakQlParser#tableSourceItem}.
	 * @param ctx the parse tree
	 */
	void exitTableSourcesItem(SpeakQlParser.TableSourcesItemContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#indexHint}.
	 * @param ctx the parse tree
	 */
	void enterIndexHint(SpeakQlParser.IndexHintContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#indexHint}.
	 * @param ctx the parse tree
	 */
	void exitIndexHint(SpeakQlParser.IndexHintContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#indexHintType}.
	 * @param ctx the parse tree
	 */
	void enterIndexHintType(SpeakQlParser.IndexHintTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#indexHintType}.
	 * @param ctx the parse tree
	 */
	void exitIndexHintType(SpeakQlParser.IndexHintTypeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code innerJoin}
	 * labeled alternative in {@link SpeakQlParser#joinPart}.
	 * @param ctx the parse tree
	 */
	void enterInnerJoin(SpeakQlParser.InnerJoinContext ctx);
	/**
	 * Exit a parse tree produced by the {@code innerJoin}
	 * labeled alternative in {@link SpeakQlParser#joinPart}.
	 * @param ctx the parse tree
	 */
	void exitInnerJoin(SpeakQlParser.InnerJoinContext ctx);
	/**
	 * Enter a parse tree produced by the {@code straightJoin}
	 * labeled alternative in {@link SpeakQlParser#joinPart}.
	 * @param ctx the parse tree
	 */
	void enterStraightJoin(SpeakQlParser.StraightJoinContext ctx);
	/**
	 * Exit a parse tree produced by the {@code straightJoin}
	 * labeled alternative in {@link SpeakQlParser#joinPart}.
	 * @param ctx the parse tree
	 */
	void exitStraightJoin(SpeakQlParser.StraightJoinContext ctx);
	/**
	 * Enter a parse tree produced by the {@code outerJoin}
	 * labeled alternative in {@link SpeakQlParser#joinPart}.
	 * @param ctx the parse tree
	 */
	void enterOuterJoin(SpeakQlParser.OuterJoinContext ctx);
	/**
	 * Exit a parse tree produced by the {@code outerJoin}
	 * labeled alternative in {@link SpeakQlParser#joinPart}.
	 * @param ctx the parse tree
	 */
	void exitOuterJoin(SpeakQlParser.OuterJoinContext ctx);
	/**
	 * Enter a parse tree produced by the {@code naturalJoin}
	 * labeled alternative in {@link SpeakQlParser#joinPart}.
	 * @param ctx the parse tree
	 */
	void enterNaturalJoin(SpeakQlParser.NaturalJoinContext ctx);
	/**
	 * Exit a parse tree produced by the {@code naturalJoin}
	 * labeled alternative in {@link SpeakQlParser#joinPart}.
	 * @param ctx the parse tree
	 */
	void exitNaturalJoin(SpeakQlParser.NaturalJoinContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#joinKeyword}.
	 * @param ctx the parse tree
	 */
	void enterJoinKeyword(SpeakQlParser.JoinKeywordContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#joinKeyword}.
	 * @param ctx the parse tree
	 */
	void exitJoinKeyword(SpeakQlParser.JoinKeywordContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#queryExpression}.
	 * @param ctx the parse tree
	 */
	void enterQueryExpression(SpeakQlParser.QueryExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#queryExpression}.
	 * @param ctx the parse tree
	 */
	void exitQueryExpression(SpeakQlParser.QueryExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#queryExpressionNointo}.
	 * @param ctx the parse tree
	 */
	void enterQueryExpressionNointo(SpeakQlParser.QueryExpressionNointoContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#queryExpressionNointo}.
	 * @param ctx the parse tree
	 */
	void exitQueryExpressionNointo(SpeakQlParser.QueryExpressionNointoContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#querySpecification}.
	 * @param ctx the parse tree
	 */
	void enterQuerySpecification(SpeakQlParser.QuerySpecificationContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#querySpecification}.
	 * @param ctx the parse tree
	 */
	void exitQuerySpecification(SpeakQlParser.QuerySpecificationContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#selectModifierExpression}.
	 * @param ctx the parse tree
	 */
	void enterSelectModifierExpression(SpeakQlParser.SelectModifierExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#selectModifierExpression}.
	 * @param ctx the parse tree
	 */
	void exitSelectModifierExpression(SpeakQlParser.SelectModifierExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#selectExpression}.
	 * @param ctx the parse tree
	 */
	void enterSelectExpression(SpeakQlParser.SelectExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#selectExpression}.
	 * @param ctx the parse tree
	 */
	void exitSelectExpression(SpeakQlParser.SelectExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#tableExpression}.
	 * @param ctx the parse tree
	 */
	void enterTableExpression(SpeakQlParser.TableExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#tableExpression}.
	 * @param ctx the parse tree
	 */
	void exitTableExpression(SpeakQlParser.TableExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#selectClause}.
	 * @param ctx the parse tree
	 */
	void enterSelectClause(SpeakQlParser.SelectClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#selectClause}.
	 * @param ctx the parse tree
	 */
	void exitSelectClause(SpeakQlParser.SelectClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#selectKeyword}.
	 * @param ctx the parse tree
	 */
	void enterSelectKeyword(SpeakQlParser.SelectKeywordContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#selectKeyword}.
	 * @param ctx the parse tree
	 */
	void exitSelectKeyword(SpeakQlParser.SelectKeywordContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#querySpecificationNointo}.
	 * @param ctx the parse tree
	 */
	void enterQuerySpecificationNointo(SpeakQlParser.QuerySpecificationNointoContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#querySpecificationNointo}.
	 * @param ctx the parse tree
	 */
	void exitQuerySpecificationNointo(SpeakQlParser.QuerySpecificationNointoContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#unionParenthesis}.
	 * @param ctx the parse tree
	 */
	void enterUnionParenthesis(SpeakQlParser.UnionParenthesisContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#unionParenthesis}.
	 * @param ctx the parse tree
	 */
	void exitUnionParenthesis(SpeakQlParser.UnionParenthesisContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#unionStatement}.
	 * @param ctx the parse tree
	 */
	void enterUnionStatement(SpeakQlParser.UnionStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#unionStatement}.
	 * @param ctx the parse tree
	 */
	void exitUnionStatement(SpeakQlParser.UnionStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#selectSpec}.
	 * @param ctx the parse tree
	 */
	void enterSelectSpec(SpeakQlParser.SelectSpecContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#selectSpec}.
	 * @param ctx the parse tree
	 */
	void exitSelectSpec(SpeakQlParser.SelectSpecContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#selectElements}.
	 * @param ctx the parse tree
	 */
	void enterSelectElements(SpeakQlParser.SelectElementsContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#selectElements}.
	 * @param ctx the parse tree
	 */
	void exitSelectElements(SpeakQlParser.SelectElementsContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#selectElementDelimiter}.
	 * @param ctx the parse tree
	 */
	void enterSelectElementDelimiter(SpeakQlParser.SelectElementDelimiterContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#selectElementDelimiter}.
	 * @param ctx the parse tree
	 */
	void exitSelectElementDelimiter(SpeakQlParser.SelectElementDelimiterContext ctx);
	/**
	 * Enter a parse tree produced by the {@code selectStarElement}
	 * labeled alternative in {@link SpeakQlParser#selectElement}.
	 * @param ctx the parse tree
	 */
	void enterSelectStarElement(SpeakQlParser.SelectStarElementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code selectStarElement}
	 * labeled alternative in {@link SpeakQlParser#selectElement}.
	 * @param ctx the parse tree
	 */
	void exitSelectStarElement(SpeakQlParser.SelectStarElementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code selectColumnElement}
	 * labeled alternative in {@link SpeakQlParser#selectElement}.
	 * @param ctx the parse tree
	 */
	void enterSelectColumnElement(SpeakQlParser.SelectColumnElementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code selectColumnElement}
	 * labeled alternative in {@link SpeakQlParser#selectElement}.
	 * @param ctx the parse tree
	 */
	void exitSelectColumnElement(SpeakQlParser.SelectColumnElementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code selectFunctionElement}
	 * labeled alternative in {@link SpeakQlParser#selectElement}.
	 * @param ctx the parse tree
	 */
	void enterSelectFunctionElement(SpeakQlParser.SelectFunctionElementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code selectFunctionElement}
	 * labeled alternative in {@link SpeakQlParser#selectElement}.
	 * @param ctx the parse tree
	 */
	void exitSelectFunctionElement(SpeakQlParser.SelectFunctionElementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code selectExpressionElement}
	 * labeled alternative in {@link SpeakQlParser#selectElement}.
	 * @param ctx the parse tree
	 */
	void enterSelectExpressionElement(SpeakQlParser.SelectExpressionElementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code selectExpressionElement}
	 * labeled alternative in {@link SpeakQlParser#selectElement}.
	 * @param ctx the parse tree
	 */
	void exitSelectExpressionElement(SpeakQlParser.SelectExpressionElementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code selectIntoVariables}
	 * labeled alternative in {@link SpeakQlParser#selectIntoExpression}.
	 * @param ctx the parse tree
	 */
	void enterSelectIntoVariables(SpeakQlParser.SelectIntoVariablesContext ctx);
	/**
	 * Exit a parse tree produced by the {@code selectIntoVariables}
	 * labeled alternative in {@link SpeakQlParser#selectIntoExpression}.
	 * @param ctx the parse tree
	 */
	void exitSelectIntoVariables(SpeakQlParser.SelectIntoVariablesContext ctx);
	/**
	 * Enter a parse tree produced by the {@code selectIntoDumpFile}
	 * labeled alternative in {@link SpeakQlParser#selectIntoExpression}.
	 * @param ctx the parse tree
	 */
	void enterSelectIntoDumpFile(SpeakQlParser.SelectIntoDumpFileContext ctx);
	/**
	 * Exit a parse tree produced by the {@code selectIntoDumpFile}
	 * labeled alternative in {@link SpeakQlParser#selectIntoExpression}.
	 * @param ctx the parse tree
	 */
	void exitSelectIntoDumpFile(SpeakQlParser.SelectIntoDumpFileContext ctx);
	/**
	 * Enter a parse tree produced by the {@code selectIntoTextFile}
	 * labeled alternative in {@link SpeakQlParser#selectIntoExpression}.
	 * @param ctx the parse tree
	 */
	void enterSelectIntoTextFile(SpeakQlParser.SelectIntoTextFileContext ctx);
	/**
	 * Exit a parse tree produced by the {@code selectIntoTextFile}
	 * labeled alternative in {@link SpeakQlParser#selectIntoExpression}.
	 * @param ctx the parse tree
	 */
	void exitSelectIntoTextFile(SpeakQlParser.SelectIntoTextFileContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#selectFieldsInto}.
	 * @param ctx the parse tree
	 */
	void enterSelectFieldsInto(SpeakQlParser.SelectFieldsIntoContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#selectFieldsInto}.
	 * @param ctx the parse tree
	 */
	void exitSelectFieldsInto(SpeakQlParser.SelectFieldsIntoContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#selectLinesInto}.
	 * @param ctx the parse tree
	 */
	void enterSelectLinesInto(SpeakQlParser.SelectLinesIntoContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#selectLinesInto}.
	 * @param ctx the parse tree
	 */
	void exitSelectLinesInto(SpeakQlParser.SelectLinesIntoContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#fromClause}.
	 * @param ctx the parse tree
	 */
	void enterFromClause(SpeakQlParser.FromClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#fromClause}.
	 * @param ctx the parse tree
	 */
	void exitFromClause(SpeakQlParser.FromClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#fromKeyword}.
	 * @param ctx the parse tree
	 */
	void enterFromKeyword(SpeakQlParser.FromKeywordContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#fromKeyword}.
	 * @param ctx the parse tree
	 */
	void exitFromKeyword(SpeakQlParser.FromKeywordContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#groupByClause}.
	 * @param ctx the parse tree
	 */
	void enterGroupByClause(SpeakQlParser.GroupByClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#groupByClause}.
	 * @param ctx the parse tree
	 */
	void exitGroupByClause(SpeakQlParser.GroupByClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#havingClause}.
	 * @param ctx the parse tree
	 */
	void enterHavingClause(SpeakQlParser.HavingClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#havingClause}.
	 * @param ctx the parse tree
	 */
	void exitHavingClause(SpeakQlParser.HavingClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#windowClause}.
	 * @param ctx the parse tree
	 */
	void enterWindowClause(SpeakQlParser.WindowClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#windowClause}.
	 * @param ctx the parse tree
	 */
	void exitWindowClause(SpeakQlParser.WindowClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#groupByItem}.
	 * @param ctx the parse tree
	 */
	void enterGroupByItem(SpeakQlParser.GroupByItemContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#groupByItem}.
	 * @param ctx the parse tree
	 */
	void exitGroupByItem(SpeakQlParser.GroupByItemContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#limitClause}.
	 * @param ctx the parse tree
	 */
	void enterLimitClause(SpeakQlParser.LimitClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#limitClause}.
	 * @param ctx the parse tree
	 */
	void exitLimitClause(SpeakQlParser.LimitClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#limitClauseAtom}.
	 * @param ctx the parse tree
	 */
	void enterLimitClauseAtom(SpeakQlParser.LimitClauseAtomContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#limitClauseAtom}.
	 * @param ctx the parse tree
	 */
	void exitLimitClauseAtom(SpeakQlParser.LimitClauseAtomContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#startTransaction}.
	 * @param ctx the parse tree
	 */
	void enterStartTransaction(SpeakQlParser.StartTransactionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#startTransaction}.
	 * @param ctx the parse tree
	 */
	void exitStartTransaction(SpeakQlParser.StartTransactionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#beginWork}.
	 * @param ctx the parse tree
	 */
	void enterBeginWork(SpeakQlParser.BeginWorkContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#beginWork}.
	 * @param ctx the parse tree
	 */
	void exitBeginWork(SpeakQlParser.BeginWorkContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#commitWork}.
	 * @param ctx the parse tree
	 */
	void enterCommitWork(SpeakQlParser.CommitWorkContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#commitWork}.
	 * @param ctx the parse tree
	 */
	void exitCommitWork(SpeakQlParser.CommitWorkContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#rollbackWork}.
	 * @param ctx the parse tree
	 */
	void enterRollbackWork(SpeakQlParser.RollbackWorkContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#rollbackWork}.
	 * @param ctx the parse tree
	 */
	void exitRollbackWork(SpeakQlParser.RollbackWorkContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#savepointStatement}.
	 * @param ctx the parse tree
	 */
	void enterSavepointStatement(SpeakQlParser.SavepointStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#savepointStatement}.
	 * @param ctx the parse tree
	 */
	void exitSavepointStatement(SpeakQlParser.SavepointStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#rollbackStatement}.
	 * @param ctx the parse tree
	 */
	void enterRollbackStatement(SpeakQlParser.RollbackStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#rollbackStatement}.
	 * @param ctx the parse tree
	 */
	void exitRollbackStatement(SpeakQlParser.RollbackStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#releaseStatement}.
	 * @param ctx the parse tree
	 */
	void enterReleaseStatement(SpeakQlParser.ReleaseStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#releaseStatement}.
	 * @param ctx the parse tree
	 */
	void exitReleaseStatement(SpeakQlParser.ReleaseStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#lockTables}.
	 * @param ctx the parse tree
	 */
	void enterLockTables(SpeakQlParser.LockTablesContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#lockTables}.
	 * @param ctx the parse tree
	 */
	void exitLockTables(SpeakQlParser.LockTablesContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#unlockTables}.
	 * @param ctx the parse tree
	 */
	void enterUnlockTables(SpeakQlParser.UnlockTablesContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#unlockTables}.
	 * @param ctx the parse tree
	 */
	void exitUnlockTables(SpeakQlParser.UnlockTablesContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#setAutocommitStatement}.
	 * @param ctx the parse tree
	 */
	void enterSetAutocommitStatement(SpeakQlParser.SetAutocommitStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#setAutocommitStatement}.
	 * @param ctx the parse tree
	 */
	void exitSetAutocommitStatement(SpeakQlParser.SetAutocommitStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#setTransactionStatement}.
	 * @param ctx the parse tree
	 */
	void enterSetTransactionStatement(SpeakQlParser.SetTransactionStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#setTransactionStatement}.
	 * @param ctx the parse tree
	 */
	void exitSetTransactionStatement(SpeakQlParser.SetTransactionStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#transactionMode}.
	 * @param ctx the parse tree
	 */
	void enterTransactionMode(SpeakQlParser.TransactionModeContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#transactionMode}.
	 * @param ctx the parse tree
	 */
	void exitTransactionMode(SpeakQlParser.TransactionModeContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#lockTableElement}.
	 * @param ctx the parse tree
	 */
	void enterLockTableElement(SpeakQlParser.LockTableElementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#lockTableElement}.
	 * @param ctx the parse tree
	 */
	void exitLockTableElement(SpeakQlParser.LockTableElementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#lockAction}.
	 * @param ctx the parse tree
	 */
	void enterLockAction(SpeakQlParser.LockActionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#lockAction}.
	 * @param ctx the parse tree
	 */
	void exitLockAction(SpeakQlParser.LockActionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#transactionOption}.
	 * @param ctx the parse tree
	 */
	void enterTransactionOption(SpeakQlParser.TransactionOptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#transactionOption}.
	 * @param ctx the parse tree
	 */
	void exitTransactionOption(SpeakQlParser.TransactionOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#transactionLevel}.
	 * @param ctx the parse tree
	 */
	void enterTransactionLevel(SpeakQlParser.TransactionLevelContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#transactionLevel}.
	 * @param ctx the parse tree
	 */
	void exitTransactionLevel(SpeakQlParser.TransactionLevelContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#changeMaster}.
	 * @param ctx the parse tree
	 */
	void enterChangeMaster(SpeakQlParser.ChangeMasterContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#changeMaster}.
	 * @param ctx the parse tree
	 */
	void exitChangeMaster(SpeakQlParser.ChangeMasterContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#changeReplicationFilter}.
	 * @param ctx the parse tree
	 */
	void enterChangeReplicationFilter(SpeakQlParser.ChangeReplicationFilterContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#changeReplicationFilter}.
	 * @param ctx the parse tree
	 */
	void exitChangeReplicationFilter(SpeakQlParser.ChangeReplicationFilterContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#purgeBinaryLogs}.
	 * @param ctx the parse tree
	 */
	void enterPurgeBinaryLogs(SpeakQlParser.PurgeBinaryLogsContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#purgeBinaryLogs}.
	 * @param ctx the parse tree
	 */
	void exitPurgeBinaryLogs(SpeakQlParser.PurgeBinaryLogsContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#resetMaster}.
	 * @param ctx the parse tree
	 */
	void enterResetMaster(SpeakQlParser.ResetMasterContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#resetMaster}.
	 * @param ctx the parse tree
	 */
	void exitResetMaster(SpeakQlParser.ResetMasterContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#resetSlave}.
	 * @param ctx the parse tree
	 */
	void enterResetSlave(SpeakQlParser.ResetSlaveContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#resetSlave}.
	 * @param ctx the parse tree
	 */
	void exitResetSlave(SpeakQlParser.ResetSlaveContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#startSlave}.
	 * @param ctx the parse tree
	 */
	void enterStartSlave(SpeakQlParser.StartSlaveContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#startSlave}.
	 * @param ctx the parse tree
	 */
	void exitStartSlave(SpeakQlParser.StartSlaveContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#stopSlave}.
	 * @param ctx the parse tree
	 */
	void enterStopSlave(SpeakQlParser.StopSlaveContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#stopSlave}.
	 * @param ctx the parse tree
	 */
	void exitStopSlave(SpeakQlParser.StopSlaveContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#startGroupReplication}.
	 * @param ctx the parse tree
	 */
	void enterStartGroupReplication(SpeakQlParser.StartGroupReplicationContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#startGroupReplication}.
	 * @param ctx the parse tree
	 */
	void exitStartGroupReplication(SpeakQlParser.StartGroupReplicationContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#stopGroupReplication}.
	 * @param ctx the parse tree
	 */
	void enterStopGroupReplication(SpeakQlParser.StopGroupReplicationContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#stopGroupReplication}.
	 * @param ctx the parse tree
	 */
	void exitStopGroupReplication(SpeakQlParser.StopGroupReplicationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code masterStringOption}
	 * labeled alternative in {@link SpeakQlParser#masterOption}.
	 * @param ctx the parse tree
	 */
	void enterMasterStringOption(SpeakQlParser.MasterStringOptionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code masterStringOption}
	 * labeled alternative in {@link SpeakQlParser#masterOption}.
	 * @param ctx the parse tree
	 */
	void exitMasterStringOption(SpeakQlParser.MasterStringOptionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code masterDecimalOption}
	 * labeled alternative in {@link SpeakQlParser#masterOption}.
	 * @param ctx the parse tree
	 */
	void enterMasterDecimalOption(SpeakQlParser.MasterDecimalOptionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code masterDecimalOption}
	 * labeled alternative in {@link SpeakQlParser#masterOption}.
	 * @param ctx the parse tree
	 */
	void exitMasterDecimalOption(SpeakQlParser.MasterDecimalOptionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code masterBoolOption}
	 * labeled alternative in {@link SpeakQlParser#masterOption}.
	 * @param ctx the parse tree
	 */
	void enterMasterBoolOption(SpeakQlParser.MasterBoolOptionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code masterBoolOption}
	 * labeled alternative in {@link SpeakQlParser#masterOption}.
	 * @param ctx the parse tree
	 */
	void exitMasterBoolOption(SpeakQlParser.MasterBoolOptionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code masterRealOption}
	 * labeled alternative in {@link SpeakQlParser#masterOption}.
	 * @param ctx the parse tree
	 */
	void enterMasterRealOption(SpeakQlParser.MasterRealOptionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code masterRealOption}
	 * labeled alternative in {@link SpeakQlParser#masterOption}.
	 * @param ctx the parse tree
	 */
	void exitMasterRealOption(SpeakQlParser.MasterRealOptionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code masterUidListOption}
	 * labeled alternative in {@link SpeakQlParser#masterOption}.
	 * @param ctx the parse tree
	 */
	void enterMasterUidListOption(SpeakQlParser.MasterUidListOptionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code masterUidListOption}
	 * labeled alternative in {@link SpeakQlParser#masterOption}.
	 * @param ctx the parse tree
	 */
	void exitMasterUidListOption(SpeakQlParser.MasterUidListOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#stringMasterOption}.
	 * @param ctx the parse tree
	 */
	void enterStringMasterOption(SpeakQlParser.StringMasterOptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#stringMasterOption}.
	 * @param ctx the parse tree
	 */
	void exitStringMasterOption(SpeakQlParser.StringMasterOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#decimalMasterOption}.
	 * @param ctx the parse tree
	 */
	void enterDecimalMasterOption(SpeakQlParser.DecimalMasterOptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#decimalMasterOption}.
	 * @param ctx the parse tree
	 */
	void exitDecimalMasterOption(SpeakQlParser.DecimalMasterOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#boolMasterOption}.
	 * @param ctx the parse tree
	 */
	void enterBoolMasterOption(SpeakQlParser.BoolMasterOptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#boolMasterOption}.
	 * @param ctx the parse tree
	 */
	void exitBoolMasterOption(SpeakQlParser.BoolMasterOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#channelOption}.
	 * @param ctx the parse tree
	 */
	void enterChannelOption(SpeakQlParser.ChannelOptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#channelOption}.
	 * @param ctx the parse tree
	 */
	void exitChannelOption(SpeakQlParser.ChannelOptionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code doDbReplication}
	 * labeled alternative in {@link SpeakQlParser#replicationFilter}.
	 * @param ctx the parse tree
	 */
	void enterDoDbReplication(SpeakQlParser.DoDbReplicationContext ctx);
	/**
	 * Exit a parse tree produced by the {@code doDbReplication}
	 * labeled alternative in {@link SpeakQlParser#replicationFilter}.
	 * @param ctx the parse tree
	 */
	void exitDoDbReplication(SpeakQlParser.DoDbReplicationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ignoreDbReplication}
	 * labeled alternative in {@link SpeakQlParser#replicationFilter}.
	 * @param ctx the parse tree
	 */
	void enterIgnoreDbReplication(SpeakQlParser.IgnoreDbReplicationContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ignoreDbReplication}
	 * labeled alternative in {@link SpeakQlParser#replicationFilter}.
	 * @param ctx the parse tree
	 */
	void exitIgnoreDbReplication(SpeakQlParser.IgnoreDbReplicationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code doTableReplication}
	 * labeled alternative in {@link SpeakQlParser#replicationFilter}.
	 * @param ctx the parse tree
	 */
	void enterDoTableReplication(SpeakQlParser.DoTableReplicationContext ctx);
	/**
	 * Exit a parse tree produced by the {@code doTableReplication}
	 * labeled alternative in {@link SpeakQlParser#replicationFilter}.
	 * @param ctx the parse tree
	 */
	void exitDoTableReplication(SpeakQlParser.DoTableReplicationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ignoreTableReplication}
	 * labeled alternative in {@link SpeakQlParser#replicationFilter}.
	 * @param ctx the parse tree
	 */
	void enterIgnoreTableReplication(SpeakQlParser.IgnoreTableReplicationContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ignoreTableReplication}
	 * labeled alternative in {@link SpeakQlParser#replicationFilter}.
	 * @param ctx the parse tree
	 */
	void exitIgnoreTableReplication(SpeakQlParser.IgnoreTableReplicationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code wildDoTableReplication}
	 * labeled alternative in {@link SpeakQlParser#replicationFilter}.
	 * @param ctx the parse tree
	 */
	void enterWildDoTableReplication(SpeakQlParser.WildDoTableReplicationContext ctx);
	/**
	 * Exit a parse tree produced by the {@code wildDoTableReplication}
	 * labeled alternative in {@link SpeakQlParser#replicationFilter}.
	 * @param ctx the parse tree
	 */
	void exitWildDoTableReplication(SpeakQlParser.WildDoTableReplicationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code wildIgnoreTableReplication}
	 * labeled alternative in {@link SpeakQlParser#replicationFilter}.
	 * @param ctx the parse tree
	 */
	void enterWildIgnoreTableReplication(SpeakQlParser.WildIgnoreTableReplicationContext ctx);
	/**
	 * Exit a parse tree produced by the {@code wildIgnoreTableReplication}
	 * labeled alternative in {@link SpeakQlParser#replicationFilter}.
	 * @param ctx the parse tree
	 */
	void exitWildIgnoreTableReplication(SpeakQlParser.WildIgnoreTableReplicationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code rewriteDbReplication}
	 * labeled alternative in {@link SpeakQlParser#replicationFilter}.
	 * @param ctx the parse tree
	 */
	void enterRewriteDbReplication(SpeakQlParser.RewriteDbReplicationContext ctx);
	/**
	 * Exit a parse tree produced by the {@code rewriteDbReplication}
	 * labeled alternative in {@link SpeakQlParser#replicationFilter}.
	 * @param ctx the parse tree
	 */
	void exitRewriteDbReplication(SpeakQlParser.RewriteDbReplicationContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#tablePair}.
	 * @param ctx the parse tree
	 */
	void enterTablePair(SpeakQlParser.TablePairContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#tablePair}.
	 * @param ctx the parse tree
	 */
	void exitTablePair(SpeakQlParser.TablePairContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#threadType}.
	 * @param ctx the parse tree
	 */
	void enterThreadType(SpeakQlParser.ThreadTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#threadType}.
	 * @param ctx the parse tree
	 */
	void exitThreadType(SpeakQlParser.ThreadTypeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code gtidsUntilOption}
	 * labeled alternative in {@link SpeakQlParser#untilOption}.
	 * @param ctx the parse tree
	 */
	void enterGtidsUntilOption(SpeakQlParser.GtidsUntilOptionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code gtidsUntilOption}
	 * labeled alternative in {@link SpeakQlParser#untilOption}.
	 * @param ctx the parse tree
	 */
	void exitGtidsUntilOption(SpeakQlParser.GtidsUntilOptionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code masterLogUntilOption}
	 * labeled alternative in {@link SpeakQlParser#untilOption}.
	 * @param ctx the parse tree
	 */
	void enterMasterLogUntilOption(SpeakQlParser.MasterLogUntilOptionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code masterLogUntilOption}
	 * labeled alternative in {@link SpeakQlParser#untilOption}.
	 * @param ctx the parse tree
	 */
	void exitMasterLogUntilOption(SpeakQlParser.MasterLogUntilOptionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code relayLogUntilOption}
	 * labeled alternative in {@link SpeakQlParser#untilOption}.
	 * @param ctx the parse tree
	 */
	void enterRelayLogUntilOption(SpeakQlParser.RelayLogUntilOptionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code relayLogUntilOption}
	 * labeled alternative in {@link SpeakQlParser#untilOption}.
	 * @param ctx the parse tree
	 */
	void exitRelayLogUntilOption(SpeakQlParser.RelayLogUntilOptionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code sqlGapsUntilOption}
	 * labeled alternative in {@link SpeakQlParser#untilOption}.
	 * @param ctx the parse tree
	 */
	void enterSqlGapsUntilOption(SpeakQlParser.SqlGapsUntilOptionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code sqlGapsUntilOption}
	 * labeled alternative in {@link SpeakQlParser#untilOption}.
	 * @param ctx the parse tree
	 */
	void exitSqlGapsUntilOption(SpeakQlParser.SqlGapsUntilOptionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code userConnectionOption}
	 * labeled alternative in {@link SpeakQlParser#connectionOption}.
	 * @param ctx the parse tree
	 */
	void enterUserConnectionOption(SpeakQlParser.UserConnectionOptionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code userConnectionOption}
	 * labeled alternative in {@link SpeakQlParser#connectionOption}.
	 * @param ctx the parse tree
	 */
	void exitUserConnectionOption(SpeakQlParser.UserConnectionOptionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code passwordConnectionOption}
	 * labeled alternative in {@link SpeakQlParser#connectionOption}.
	 * @param ctx the parse tree
	 */
	void enterPasswordConnectionOption(SpeakQlParser.PasswordConnectionOptionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code passwordConnectionOption}
	 * labeled alternative in {@link SpeakQlParser#connectionOption}.
	 * @param ctx the parse tree
	 */
	void exitPasswordConnectionOption(SpeakQlParser.PasswordConnectionOptionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code defaultAuthConnectionOption}
	 * labeled alternative in {@link SpeakQlParser#connectionOption}.
	 * @param ctx the parse tree
	 */
	void enterDefaultAuthConnectionOption(SpeakQlParser.DefaultAuthConnectionOptionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code defaultAuthConnectionOption}
	 * labeled alternative in {@link SpeakQlParser#connectionOption}.
	 * @param ctx the parse tree
	 */
	void exitDefaultAuthConnectionOption(SpeakQlParser.DefaultAuthConnectionOptionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code pluginDirConnectionOption}
	 * labeled alternative in {@link SpeakQlParser#connectionOption}.
	 * @param ctx the parse tree
	 */
	void enterPluginDirConnectionOption(SpeakQlParser.PluginDirConnectionOptionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code pluginDirConnectionOption}
	 * labeled alternative in {@link SpeakQlParser#connectionOption}.
	 * @param ctx the parse tree
	 */
	void exitPluginDirConnectionOption(SpeakQlParser.PluginDirConnectionOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#gtuidSet}.
	 * @param ctx the parse tree
	 */
	void enterGtuidSet(SpeakQlParser.GtuidSetContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#gtuidSet}.
	 * @param ctx the parse tree
	 */
	void exitGtuidSet(SpeakQlParser.GtuidSetContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#xaStartTransaction}.
	 * @param ctx the parse tree
	 */
	void enterXaStartTransaction(SpeakQlParser.XaStartTransactionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#xaStartTransaction}.
	 * @param ctx the parse tree
	 */
	void exitXaStartTransaction(SpeakQlParser.XaStartTransactionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#xaEndTransaction}.
	 * @param ctx the parse tree
	 */
	void enterXaEndTransaction(SpeakQlParser.XaEndTransactionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#xaEndTransaction}.
	 * @param ctx the parse tree
	 */
	void exitXaEndTransaction(SpeakQlParser.XaEndTransactionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#xaPrepareStatement}.
	 * @param ctx the parse tree
	 */
	void enterXaPrepareStatement(SpeakQlParser.XaPrepareStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#xaPrepareStatement}.
	 * @param ctx the parse tree
	 */
	void exitXaPrepareStatement(SpeakQlParser.XaPrepareStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#xaCommitWork}.
	 * @param ctx the parse tree
	 */
	void enterXaCommitWork(SpeakQlParser.XaCommitWorkContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#xaCommitWork}.
	 * @param ctx the parse tree
	 */
	void exitXaCommitWork(SpeakQlParser.XaCommitWorkContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#xaRollbackWork}.
	 * @param ctx the parse tree
	 */
	void enterXaRollbackWork(SpeakQlParser.XaRollbackWorkContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#xaRollbackWork}.
	 * @param ctx the parse tree
	 */
	void exitXaRollbackWork(SpeakQlParser.XaRollbackWorkContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#xaRecoverWork}.
	 * @param ctx the parse tree
	 */
	void enterXaRecoverWork(SpeakQlParser.XaRecoverWorkContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#xaRecoverWork}.
	 * @param ctx the parse tree
	 */
	void exitXaRecoverWork(SpeakQlParser.XaRecoverWorkContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#prepareStatement}.
	 * @param ctx the parse tree
	 */
	void enterPrepareStatement(SpeakQlParser.PrepareStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#prepareStatement}.
	 * @param ctx the parse tree
	 */
	void exitPrepareStatement(SpeakQlParser.PrepareStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#executeStatement}.
	 * @param ctx the parse tree
	 */
	void enterExecuteStatement(SpeakQlParser.ExecuteStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#executeStatement}.
	 * @param ctx the parse tree
	 */
	void exitExecuteStatement(SpeakQlParser.ExecuteStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#deallocatePrepare}.
	 * @param ctx the parse tree
	 */
	void enterDeallocatePrepare(SpeakQlParser.DeallocatePrepareContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#deallocatePrepare}.
	 * @param ctx the parse tree
	 */
	void exitDeallocatePrepare(SpeakQlParser.DeallocatePrepareContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#routineBody}.
	 * @param ctx the parse tree
	 */
	void enterRoutineBody(SpeakQlParser.RoutineBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#routineBody}.
	 * @param ctx the parse tree
	 */
	void exitRoutineBody(SpeakQlParser.RoutineBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#blockStatement}.
	 * @param ctx the parse tree
	 */
	void enterBlockStatement(SpeakQlParser.BlockStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#blockStatement}.
	 * @param ctx the parse tree
	 */
	void exitBlockStatement(SpeakQlParser.BlockStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#caseStatement}.
	 * @param ctx the parse tree
	 */
	void enterCaseStatement(SpeakQlParser.CaseStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#caseStatement}.
	 * @param ctx the parse tree
	 */
	void exitCaseStatement(SpeakQlParser.CaseStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(SpeakQlParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(SpeakQlParser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#iterateStatement}.
	 * @param ctx the parse tree
	 */
	void enterIterateStatement(SpeakQlParser.IterateStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#iterateStatement}.
	 * @param ctx the parse tree
	 */
	void exitIterateStatement(SpeakQlParser.IterateStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#leaveStatement}.
	 * @param ctx the parse tree
	 */
	void enterLeaveStatement(SpeakQlParser.LeaveStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#leaveStatement}.
	 * @param ctx the parse tree
	 */
	void exitLeaveStatement(SpeakQlParser.LeaveStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#loopStatement}.
	 * @param ctx the parse tree
	 */
	void enterLoopStatement(SpeakQlParser.LoopStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#loopStatement}.
	 * @param ctx the parse tree
	 */
	void exitLoopStatement(SpeakQlParser.LoopStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#repeatStatement}.
	 * @param ctx the parse tree
	 */
	void enterRepeatStatement(SpeakQlParser.RepeatStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#repeatStatement}.
	 * @param ctx the parse tree
	 */
	void exitRepeatStatement(SpeakQlParser.RepeatStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void enterReturnStatement(SpeakQlParser.ReturnStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void exitReturnStatement(SpeakQlParser.ReturnStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void enterWhileStatement(SpeakQlParser.WhileStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void exitWhileStatement(SpeakQlParser.WhileStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code CloseCursor}
	 * labeled alternative in {@link SpeakQlParser#cursorStatement}.
	 * @param ctx the parse tree
	 */
	void enterCloseCursor(SpeakQlParser.CloseCursorContext ctx);
	/**
	 * Exit a parse tree produced by the {@code CloseCursor}
	 * labeled alternative in {@link SpeakQlParser#cursorStatement}.
	 * @param ctx the parse tree
	 */
	void exitCloseCursor(SpeakQlParser.CloseCursorContext ctx);
	/**
	 * Enter a parse tree produced by the {@code FetchCursor}
	 * labeled alternative in {@link SpeakQlParser#cursorStatement}.
	 * @param ctx the parse tree
	 */
	void enterFetchCursor(SpeakQlParser.FetchCursorContext ctx);
	/**
	 * Exit a parse tree produced by the {@code FetchCursor}
	 * labeled alternative in {@link SpeakQlParser#cursorStatement}.
	 * @param ctx the parse tree
	 */
	void exitFetchCursor(SpeakQlParser.FetchCursorContext ctx);
	/**
	 * Enter a parse tree produced by the {@code OpenCursor}
	 * labeled alternative in {@link SpeakQlParser#cursorStatement}.
	 * @param ctx the parse tree
	 */
	void enterOpenCursor(SpeakQlParser.OpenCursorContext ctx);
	/**
	 * Exit a parse tree produced by the {@code OpenCursor}
	 * labeled alternative in {@link SpeakQlParser#cursorStatement}.
	 * @param ctx the parse tree
	 */
	void exitOpenCursor(SpeakQlParser.OpenCursorContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#declareVariable}.
	 * @param ctx the parse tree
	 */
	void enterDeclareVariable(SpeakQlParser.DeclareVariableContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#declareVariable}.
	 * @param ctx the parse tree
	 */
	void exitDeclareVariable(SpeakQlParser.DeclareVariableContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#declareCondition}.
	 * @param ctx the parse tree
	 */
	void enterDeclareCondition(SpeakQlParser.DeclareConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#declareCondition}.
	 * @param ctx the parse tree
	 */
	void exitDeclareCondition(SpeakQlParser.DeclareConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#declareCursor}.
	 * @param ctx the parse tree
	 */
	void enterDeclareCursor(SpeakQlParser.DeclareCursorContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#declareCursor}.
	 * @param ctx the parse tree
	 */
	void exitDeclareCursor(SpeakQlParser.DeclareCursorContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#declareHandler}.
	 * @param ctx the parse tree
	 */
	void enterDeclareHandler(SpeakQlParser.DeclareHandlerContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#declareHandler}.
	 * @param ctx the parse tree
	 */
	void exitDeclareHandler(SpeakQlParser.DeclareHandlerContext ctx);
	/**
	 * Enter a parse tree produced by the {@code handlerConditionCode}
	 * labeled alternative in {@link SpeakQlParser#handlerConditionValue}.
	 * @param ctx the parse tree
	 */
	void enterHandlerConditionCode(SpeakQlParser.HandlerConditionCodeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code handlerConditionCode}
	 * labeled alternative in {@link SpeakQlParser#handlerConditionValue}.
	 * @param ctx the parse tree
	 */
	void exitHandlerConditionCode(SpeakQlParser.HandlerConditionCodeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code handlerConditionState}
	 * labeled alternative in {@link SpeakQlParser#handlerConditionValue}.
	 * @param ctx the parse tree
	 */
	void enterHandlerConditionState(SpeakQlParser.HandlerConditionStateContext ctx);
	/**
	 * Exit a parse tree produced by the {@code handlerConditionState}
	 * labeled alternative in {@link SpeakQlParser#handlerConditionValue}.
	 * @param ctx the parse tree
	 */
	void exitHandlerConditionState(SpeakQlParser.HandlerConditionStateContext ctx);
	/**
	 * Enter a parse tree produced by the {@code handlerConditionName}
	 * labeled alternative in {@link SpeakQlParser#handlerConditionValue}.
	 * @param ctx the parse tree
	 */
	void enterHandlerConditionName(SpeakQlParser.HandlerConditionNameContext ctx);
	/**
	 * Exit a parse tree produced by the {@code handlerConditionName}
	 * labeled alternative in {@link SpeakQlParser#handlerConditionValue}.
	 * @param ctx the parse tree
	 */
	void exitHandlerConditionName(SpeakQlParser.HandlerConditionNameContext ctx);
	/**
	 * Enter a parse tree produced by the {@code handlerConditionWarning}
	 * labeled alternative in {@link SpeakQlParser#handlerConditionValue}.
	 * @param ctx the parse tree
	 */
	void enterHandlerConditionWarning(SpeakQlParser.HandlerConditionWarningContext ctx);
	/**
	 * Exit a parse tree produced by the {@code handlerConditionWarning}
	 * labeled alternative in {@link SpeakQlParser#handlerConditionValue}.
	 * @param ctx the parse tree
	 */
	void exitHandlerConditionWarning(SpeakQlParser.HandlerConditionWarningContext ctx);
	/**
	 * Enter a parse tree produced by the {@code handlerConditionNotfound}
	 * labeled alternative in {@link SpeakQlParser#handlerConditionValue}.
	 * @param ctx the parse tree
	 */
	void enterHandlerConditionNotfound(SpeakQlParser.HandlerConditionNotfoundContext ctx);
	/**
	 * Exit a parse tree produced by the {@code handlerConditionNotfound}
	 * labeled alternative in {@link SpeakQlParser#handlerConditionValue}.
	 * @param ctx the parse tree
	 */
	void exitHandlerConditionNotfound(SpeakQlParser.HandlerConditionNotfoundContext ctx);
	/**
	 * Enter a parse tree produced by the {@code handlerConditionException}
	 * labeled alternative in {@link SpeakQlParser#handlerConditionValue}.
	 * @param ctx the parse tree
	 */
	void enterHandlerConditionException(SpeakQlParser.HandlerConditionExceptionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code handlerConditionException}
	 * labeled alternative in {@link SpeakQlParser#handlerConditionValue}.
	 * @param ctx the parse tree
	 */
	void exitHandlerConditionException(SpeakQlParser.HandlerConditionExceptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#procedureSqlStatement}.
	 * @param ctx the parse tree
	 */
	void enterProcedureSqlStatement(SpeakQlParser.ProcedureSqlStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#procedureSqlStatement}.
	 * @param ctx the parse tree
	 */
	void exitProcedureSqlStatement(SpeakQlParser.ProcedureSqlStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#caseAlternative}.
	 * @param ctx the parse tree
	 */
	void enterCaseAlternative(SpeakQlParser.CaseAlternativeContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#caseAlternative}.
	 * @param ctx the parse tree
	 */
	void exitCaseAlternative(SpeakQlParser.CaseAlternativeContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#elifAlternative}.
	 * @param ctx the parse tree
	 */
	void enterElifAlternative(SpeakQlParser.ElifAlternativeContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#elifAlternative}.
	 * @param ctx the parse tree
	 */
	void exitElifAlternative(SpeakQlParser.ElifAlternativeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alterUserMysqlV56}
	 * labeled alternative in {@link SpeakQlParser#alterUser}.
	 * @param ctx the parse tree
	 */
	void enterAlterUserMysqlV56(SpeakQlParser.AlterUserMysqlV56Context ctx);
	/**
	 * Exit a parse tree produced by the {@code alterUserMysqlV56}
	 * labeled alternative in {@link SpeakQlParser#alterUser}.
	 * @param ctx the parse tree
	 */
	void exitAlterUserMysqlV56(SpeakQlParser.AlterUserMysqlV56Context ctx);
	/**
	 * Enter a parse tree produced by the {@code alterUserMysqlV57}
	 * labeled alternative in {@link SpeakQlParser#alterUser}.
	 * @param ctx the parse tree
	 */
	void enterAlterUserMysqlV57(SpeakQlParser.AlterUserMysqlV57Context ctx);
	/**
	 * Exit a parse tree produced by the {@code alterUserMysqlV57}
	 * labeled alternative in {@link SpeakQlParser#alterUser}.
	 * @param ctx the parse tree
	 */
	void exitAlterUserMysqlV57(SpeakQlParser.AlterUserMysqlV57Context ctx);
	/**
	 * Enter a parse tree produced by the {@code createUserMysqlV56}
	 * labeled alternative in {@link SpeakQlParser#createUser}.
	 * @param ctx the parse tree
	 */
	void enterCreateUserMysqlV56(SpeakQlParser.CreateUserMysqlV56Context ctx);
	/**
	 * Exit a parse tree produced by the {@code createUserMysqlV56}
	 * labeled alternative in {@link SpeakQlParser#createUser}.
	 * @param ctx the parse tree
	 */
	void exitCreateUserMysqlV56(SpeakQlParser.CreateUserMysqlV56Context ctx);
	/**
	 * Enter a parse tree produced by the {@code createUserMysqlV57}
	 * labeled alternative in {@link SpeakQlParser#createUser}.
	 * @param ctx the parse tree
	 */
	void enterCreateUserMysqlV57(SpeakQlParser.CreateUserMysqlV57Context ctx);
	/**
	 * Exit a parse tree produced by the {@code createUserMysqlV57}
	 * labeled alternative in {@link SpeakQlParser#createUser}.
	 * @param ctx the parse tree
	 */
	void exitCreateUserMysqlV57(SpeakQlParser.CreateUserMysqlV57Context ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#dropUser}.
	 * @param ctx the parse tree
	 */
	void enterDropUser(SpeakQlParser.DropUserContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#dropUser}.
	 * @param ctx the parse tree
	 */
	void exitDropUser(SpeakQlParser.DropUserContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#grantStatement}.
	 * @param ctx the parse tree
	 */
	void enterGrantStatement(SpeakQlParser.GrantStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#grantStatement}.
	 * @param ctx the parse tree
	 */
	void exitGrantStatement(SpeakQlParser.GrantStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#roleOption}.
	 * @param ctx the parse tree
	 */
	void enterRoleOption(SpeakQlParser.RoleOptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#roleOption}.
	 * @param ctx the parse tree
	 */
	void exitRoleOption(SpeakQlParser.RoleOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#grantProxy}.
	 * @param ctx the parse tree
	 */
	void enterGrantProxy(SpeakQlParser.GrantProxyContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#grantProxy}.
	 * @param ctx the parse tree
	 */
	void exitGrantProxy(SpeakQlParser.GrantProxyContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#renameUser}.
	 * @param ctx the parse tree
	 */
	void enterRenameUser(SpeakQlParser.RenameUserContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#renameUser}.
	 * @param ctx the parse tree
	 */
	void exitRenameUser(SpeakQlParser.RenameUserContext ctx);
	/**
	 * Enter a parse tree produced by the {@code detailRevoke}
	 * labeled alternative in {@link SpeakQlParser#revokeStatement}.
	 * @param ctx the parse tree
	 */
	void enterDetailRevoke(SpeakQlParser.DetailRevokeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code detailRevoke}
	 * labeled alternative in {@link SpeakQlParser#revokeStatement}.
	 * @param ctx the parse tree
	 */
	void exitDetailRevoke(SpeakQlParser.DetailRevokeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code shortRevoke}
	 * labeled alternative in {@link SpeakQlParser#revokeStatement}.
	 * @param ctx the parse tree
	 */
	void enterShortRevoke(SpeakQlParser.ShortRevokeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code shortRevoke}
	 * labeled alternative in {@link SpeakQlParser#revokeStatement}.
	 * @param ctx the parse tree
	 */
	void exitShortRevoke(SpeakQlParser.ShortRevokeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code roleRevoke}
	 * labeled alternative in {@link SpeakQlParser#revokeStatement}.
	 * @param ctx the parse tree
	 */
	void enterRoleRevoke(SpeakQlParser.RoleRevokeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code roleRevoke}
	 * labeled alternative in {@link SpeakQlParser#revokeStatement}.
	 * @param ctx the parse tree
	 */
	void exitRoleRevoke(SpeakQlParser.RoleRevokeContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#revokeProxy}.
	 * @param ctx the parse tree
	 */
	void enterRevokeProxy(SpeakQlParser.RevokeProxyContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#revokeProxy}.
	 * @param ctx the parse tree
	 */
	void exitRevokeProxy(SpeakQlParser.RevokeProxyContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#setPasswordStatement}.
	 * @param ctx the parse tree
	 */
	void enterSetPasswordStatement(SpeakQlParser.SetPasswordStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#setPasswordStatement}.
	 * @param ctx the parse tree
	 */
	void exitSetPasswordStatement(SpeakQlParser.SetPasswordStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#userSpecification}.
	 * @param ctx the parse tree
	 */
	void enterUserSpecification(SpeakQlParser.UserSpecificationContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#userSpecification}.
	 * @param ctx the parse tree
	 */
	void exitUserSpecification(SpeakQlParser.UserSpecificationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code passwordAuthOption}
	 * labeled alternative in {@link SpeakQlParser#userAuthOption}.
	 * @param ctx the parse tree
	 */
	void enterPasswordAuthOption(SpeakQlParser.PasswordAuthOptionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code passwordAuthOption}
	 * labeled alternative in {@link SpeakQlParser#userAuthOption}.
	 * @param ctx the parse tree
	 */
	void exitPasswordAuthOption(SpeakQlParser.PasswordAuthOptionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code stringAuthOption}
	 * labeled alternative in {@link SpeakQlParser#userAuthOption}.
	 * @param ctx the parse tree
	 */
	void enterStringAuthOption(SpeakQlParser.StringAuthOptionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code stringAuthOption}
	 * labeled alternative in {@link SpeakQlParser#userAuthOption}.
	 * @param ctx the parse tree
	 */
	void exitStringAuthOption(SpeakQlParser.StringAuthOptionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code hashAuthOption}
	 * labeled alternative in {@link SpeakQlParser#userAuthOption}.
	 * @param ctx the parse tree
	 */
	void enterHashAuthOption(SpeakQlParser.HashAuthOptionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code hashAuthOption}
	 * labeled alternative in {@link SpeakQlParser#userAuthOption}.
	 * @param ctx the parse tree
	 */
	void exitHashAuthOption(SpeakQlParser.HashAuthOptionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code simpleAuthOption}
	 * labeled alternative in {@link SpeakQlParser#userAuthOption}.
	 * @param ctx the parse tree
	 */
	void enterSimpleAuthOption(SpeakQlParser.SimpleAuthOptionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code simpleAuthOption}
	 * labeled alternative in {@link SpeakQlParser#userAuthOption}.
	 * @param ctx the parse tree
	 */
	void exitSimpleAuthOption(SpeakQlParser.SimpleAuthOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#tlsOption}.
	 * @param ctx the parse tree
	 */
	void enterTlsOption(SpeakQlParser.TlsOptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#tlsOption}.
	 * @param ctx the parse tree
	 */
	void exitTlsOption(SpeakQlParser.TlsOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#userResourceOption}.
	 * @param ctx the parse tree
	 */
	void enterUserResourceOption(SpeakQlParser.UserResourceOptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#userResourceOption}.
	 * @param ctx the parse tree
	 */
	void exitUserResourceOption(SpeakQlParser.UserResourceOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#userPasswordOption}.
	 * @param ctx the parse tree
	 */
	void enterUserPasswordOption(SpeakQlParser.UserPasswordOptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#userPasswordOption}.
	 * @param ctx the parse tree
	 */
	void exitUserPasswordOption(SpeakQlParser.UserPasswordOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#userLockOption}.
	 * @param ctx the parse tree
	 */
	void enterUserLockOption(SpeakQlParser.UserLockOptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#userLockOption}.
	 * @param ctx the parse tree
	 */
	void exitUserLockOption(SpeakQlParser.UserLockOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#privelegeClause}.
	 * @param ctx the parse tree
	 */
	void enterPrivelegeClause(SpeakQlParser.PrivelegeClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#privelegeClause}.
	 * @param ctx the parse tree
	 */
	void exitPrivelegeClause(SpeakQlParser.PrivelegeClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#privilege}.
	 * @param ctx the parse tree
	 */
	void enterPrivilege(SpeakQlParser.PrivilegeContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#privilege}.
	 * @param ctx the parse tree
	 */
	void exitPrivilege(SpeakQlParser.PrivilegeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code currentSchemaPriviLevel}
	 * labeled alternative in {@link SpeakQlParser#privilegeLevel}.
	 * @param ctx the parse tree
	 */
	void enterCurrentSchemaPriviLevel(SpeakQlParser.CurrentSchemaPriviLevelContext ctx);
	/**
	 * Exit a parse tree produced by the {@code currentSchemaPriviLevel}
	 * labeled alternative in {@link SpeakQlParser#privilegeLevel}.
	 * @param ctx the parse tree
	 */
	void exitCurrentSchemaPriviLevel(SpeakQlParser.CurrentSchemaPriviLevelContext ctx);
	/**
	 * Enter a parse tree produced by the {@code globalPrivLevel}
	 * labeled alternative in {@link SpeakQlParser#privilegeLevel}.
	 * @param ctx the parse tree
	 */
	void enterGlobalPrivLevel(SpeakQlParser.GlobalPrivLevelContext ctx);
	/**
	 * Exit a parse tree produced by the {@code globalPrivLevel}
	 * labeled alternative in {@link SpeakQlParser#privilegeLevel}.
	 * @param ctx the parse tree
	 */
	void exitGlobalPrivLevel(SpeakQlParser.GlobalPrivLevelContext ctx);
	/**
	 * Enter a parse tree produced by the {@code definiteSchemaPrivLevel}
	 * labeled alternative in {@link SpeakQlParser#privilegeLevel}.
	 * @param ctx the parse tree
	 */
	void enterDefiniteSchemaPrivLevel(SpeakQlParser.DefiniteSchemaPrivLevelContext ctx);
	/**
	 * Exit a parse tree produced by the {@code definiteSchemaPrivLevel}
	 * labeled alternative in {@link SpeakQlParser#privilegeLevel}.
	 * @param ctx the parse tree
	 */
	void exitDefiniteSchemaPrivLevel(SpeakQlParser.DefiniteSchemaPrivLevelContext ctx);
	/**
	 * Enter a parse tree produced by the {@code definiteFullTablePrivLevel}
	 * labeled alternative in {@link SpeakQlParser#privilegeLevel}.
	 * @param ctx the parse tree
	 */
	void enterDefiniteFullTablePrivLevel(SpeakQlParser.DefiniteFullTablePrivLevelContext ctx);
	/**
	 * Exit a parse tree produced by the {@code definiteFullTablePrivLevel}
	 * labeled alternative in {@link SpeakQlParser#privilegeLevel}.
	 * @param ctx the parse tree
	 */
	void exitDefiniteFullTablePrivLevel(SpeakQlParser.DefiniteFullTablePrivLevelContext ctx);
	/**
	 * Enter a parse tree produced by the {@code definiteFullTablePrivLevel2}
	 * labeled alternative in {@link SpeakQlParser#privilegeLevel}.
	 * @param ctx the parse tree
	 */
	void enterDefiniteFullTablePrivLevel2(SpeakQlParser.DefiniteFullTablePrivLevel2Context ctx);
	/**
	 * Exit a parse tree produced by the {@code definiteFullTablePrivLevel2}
	 * labeled alternative in {@link SpeakQlParser#privilegeLevel}.
	 * @param ctx the parse tree
	 */
	void exitDefiniteFullTablePrivLevel2(SpeakQlParser.DefiniteFullTablePrivLevel2Context ctx);
	/**
	 * Enter a parse tree produced by the {@code definiteTablePrivLevel}
	 * labeled alternative in {@link SpeakQlParser#privilegeLevel}.
	 * @param ctx the parse tree
	 */
	void enterDefiniteTablePrivLevel(SpeakQlParser.DefiniteTablePrivLevelContext ctx);
	/**
	 * Exit a parse tree produced by the {@code definiteTablePrivLevel}
	 * labeled alternative in {@link SpeakQlParser#privilegeLevel}.
	 * @param ctx the parse tree
	 */
	void exitDefiniteTablePrivLevel(SpeakQlParser.DefiniteTablePrivLevelContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#renameUserClause}.
	 * @param ctx the parse tree
	 */
	void enterRenameUserClause(SpeakQlParser.RenameUserClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#renameUserClause}.
	 * @param ctx the parse tree
	 */
	void exitRenameUserClause(SpeakQlParser.RenameUserClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#analyzeTable}.
	 * @param ctx the parse tree
	 */
	void enterAnalyzeTable(SpeakQlParser.AnalyzeTableContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#analyzeTable}.
	 * @param ctx the parse tree
	 */
	void exitAnalyzeTable(SpeakQlParser.AnalyzeTableContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#checkTable}.
	 * @param ctx the parse tree
	 */
	void enterCheckTable(SpeakQlParser.CheckTableContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#checkTable}.
	 * @param ctx the parse tree
	 */
	void exitCheckTable(SpeakQlParser.CheckTableContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#checksumTable}.
	 * @param ctx the parse tree
	 */
	void enterChecksumTable(SpeakQlParser.ChecksumTableContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#checksumTable}.
	 * @param ctx the parse tree
	 */
	void exitChecksumTable(SpeakQlParser.ChecksumTableContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#optimizeTable}.
	 * @param ctx the parse tree
	 */
	void enterOptimizeTable(SpeakQlParser.OptimizeTableContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#optimizeTable}.
	 * @param ctx the parse tree
	 */
	void exitOptimizeTable(SpeakQlParser.OptimizeTableContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#repairTable}.
	 * @param ctx the parse tree
	 */
	void enterRepairTable(SpeakQlParser.RepairTableContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#repairTable}.
	 * @param ctx the parse tree
	 */
	void exitRepairTable(SpeakQlParser.RepairTableContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#checkTableOption}.
	 * @param ctx the parse tree
	 */
	void enterCheckTableOption(SpeakQlParser.CheckTableOptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#checkTableOption}.
	 * @param ctx the parse tree
	 */
	void exitCheckTableOption(SpeakQlParser.CheckTableOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#createUdfunction}.
	 * @param ctx the parse tree
	 */
	void enterCreateUdfunction(SpeakQlParser.CreateUdfunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#createUdfunction}.
	 * @param ctx the parse tree
	 */
	void exitCreateUdfunction(SpeakQlParser.CreateUdfunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#installPlugin}.
	 * @param ctx the parse tree
	 */
	void enterInstallPlugin(SpeakQlParser.InstallPluginContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#installPlugin}.
	 * @param ctx the parse tree
	 */
	void exitInstallPlugin(SpeakQlParser.InstallPluginContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#uninstallPlugin}.
	 * @param ctx the parse tree
	 */
	void enterUninstallPlugin(SpeakQlParser.UninstallPluginContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#uninstallPlugin}.
	 * @param ctx the parse tree
	 */
	void exitUninstallPlugin(SpeakQlParser.UninstallPluginContext ctx);
	/**
	 * Enter a parse tree produced by the {@code setVariable}
	 * labeled alternative in {@link SpeakQlParser#setStatement}.
	 * @param ctx the parse tree
	 */
	void enterSetVariable(SpeakQlParser.SetVariableContext ctx);
	/**
	 * Exit a parse tree produced by the {@code setVariable}
	 * labeled alternative in {@link SpeakQlParser#setStatement}.
	 * @param ctx the parse tree
	 */
	void exitSetVariable(SpeakQlParser.SetVariableContext ctx);
	/**
	 * Enter a parse tree produced by the {@code setCharset}
	 * labeled alternative in {@link SpeakQlParser#setStatement}.
	 * @param ctx the parse tree
	 */
	void enterSetCharset(SpeakQlParser.SetCharsetContext ctx);
	/**
	 * Exit a parse tree produced by the {@code setCharset}
	 * labeled alternative in {@link SpeakQlParser#setStatement}.
	 * @param ctx the parse tree
	 */
	void exitSetCharset(SpeakQlParser.SetCharsetContext ctx);
	/**
	 * Enter a parse tree produced by the {@code setNames}
	 * labeled alternative in {@link SpeakQlParser#setStatement}.
	 * @param ctx the parse tree
	 */
	void enterSetNames(SpeakQlParser.SetNamesContext ctx);
	/**
	 * Exit a parse tree produced by the {@code setNames}
	 * labeled alternative in {@link SpeakQlParser#setStatement}.
	 * @param ctx the parse tree
	 */
	void exitSetNames(SpeakQlParser.SetNamesContext ctx);
	/**
	 * Enter a parse tree produced by the {@code setPassword}
	 * labeled alternative in {@link SpeakQlParser#setStatement}.
	 * @param ctx the parse tree
	 */
	void enterSetPassword(SpeakQlParser.SetPasswordContext ctx);
	/**
	 * Exit a parse tree produced by the {@code setPassword}
	 * labeled alternative in {@link SpeakQlParser#setStatement}.
	 * @param ctx the parse tree
	 */
	void exitSetPassword(SpeakQlParser.SetPasswordContext ctx);
	/**
	 * Enter a parse tree produced by the {@code setTransaction}
	 * labeled alternative in {@link SpeakQlParser#setStatement}.
	 * @param ctx the parse tree
	 */
	void enterSetTransaction(SpeakQlParser.SetTransactionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code setTransaction}
	 * labeled alternative in {@link SpeakQlParser#setStatement}.
	 * @param ctx the parse tree
	 */
	void exitSetTransaction(SpeakQlParser.SetTransactionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code setAutocommit}
	 * labeled alternative in {@link SpeakQlParser#setStatement}.
	 * @param ctx the parse tree
	 */
	void enterSetAutocommit(SpeakQlParser.SetAutocommitContext ctx);
	/**
	 * Exit a parse tree produced by the {@code setAutocommit}
	 * labeled alternative in {@link SpeakQlParser#setStatement}.
	 * @param ctx the parse tree
	 */
	void exitSetAutocommit(SpeakQlParser.SetAutocommitContext ctx);
	/**
	 * Enter a parse tree produced by the {@code setNewValueInsideTrigger}
	 * labeled alternative in {@link SpeakQlParser#setStatement}.
	 * @param ctx the parse tree
	 */
	void enterSetNewValueInsideTrigger(SpeakQlParser.SetNewValueInsideTriggerContext ctx);
	/**
	 * Exit a parse tree produced by the {@code setNewValueInsideTrigger}
	 * labeled alternative in {@link SpeakQlParser#setStatement}.
	 * @param ctx the parse tree
	 */
	void exitSetNewValueInsideTrigger(SpeakQlParser.SetNewValueInsideTriggerContext ctx);
	/**
	 * Enter a parse tree produced by the {@code showMasterLogs}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void enterShowMasterLogs(SpeakQlParser.ShowMasterLogsContext ctx);
	/**
	 * Exit a parse tree produced by the {@code showMasterLogs}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void exitShowMasterLogs(SpeakQlParser.ShowMasterLogsContext ctx);
	/**
	 * Enter a parse tree produced by the {@code showLogEvents}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void enterShowLogEvents(SpeakQlParser.ShowLogEventsContext ctx);
	/**
	 * Exit a parse tree produced by the {@code showLogEvents}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void exitShowLogEvents(SpeakQlParser.ShowLogEventsContext ctx);
	/**
	 * Enter a parse tree produced by the {@code showObjectFilter}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void enterShowObjectFilter(SpeakQlParser.ShowObjectFilterContext ctx);
	/**
	 * Exit a parse tree produced by the {@code showObjectFilter}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void exitShowObjectFilter(SpeakQlParser.ShowObjectFilterContext ctx);
	/**
	 * Enter a parse tree produced by the {@code showColumns}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void enterShowColumns(SpeakQlParser.ShowColumnsContext ctx);
	/**
	 * Exit a parse tree produced by the {@code showColumns}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void exitShowColumns(SpeakQlParser.ShowColumnsContext ctx);
	/**
	 * Enter a parse tree produced by the {@code showCreateDb}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void enterShowCreateDb(SpeakQlParser.ShowCreateDbContext ctx);
	/**
	 * Exit a parse tree produced by the {@code showCreateDb}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void exitShowCreateDb(SpeakQlParser.ShowCreateDbContext ctx);
	/**
	 * Enter a parse tree produced by the {@code showCreateFullIdObject}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void enterShowCreateFullIdObject(SpeakQlParser.ShowCreateFullIdObjectContext ctx);
	/**
	 * Exit a parse tree produced by the {@code showCreateFullIdObject}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void exitShowCreateFullIdObject(SpeakQlParser.ShowCreateFullIdObjectContext ctx);
	/**
	 * Enter a parse tree produced by the {@code showCreateUser}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void enterShowCreateUser(SpeakQlParser.ShowCreateUserContext ctx);
	/**
	 * Exit a parse tree produced by the {@code showCreateUser}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void exitShowCreateUser(SpeakQlParser.ShowCreateUserContext ctx);
	/**
	 * Enter a parse tree produced by the {@code showEngine}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void enterShowEngine(SpeakQlParser.ShowEngineContext ctx);
	/**
	 * Exit a parse tree produced by the {@code showEngine}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void exitShowEngine(SpeakQlParser.ShowEngineContext ctx);
	/**
	 * Enter a parse tree produced by the {@code showGlobalInfo}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void enterShowGlobalInfo(SpeakQlParser.ShowGlobalInfoContext ctx);
	/**
	 * Exit a parse tree produced by the {@code showGlobalInfo}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void exitShowGlobalInfo(SpeakQlParser.ShowGlobalInfoContext ctx);
	/**
	 * Enter a parse tree produced by the {@code showErrors}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void enterShowErrors(SpeakQlParser.ShowErrorsContext ctx);
	/**
	 * Exit a parse tree produced by the {@code showErrors}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void exitShowErrors(SpeakQlParser.ShowErrorsContext ctx);
	/**
	 * Enter a parse tree produced by the {@code showCountErrors}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void enterShowCountErrors(SpeakQlParser.ShowCountErrorsContext ctx);
	/**
	 * Exit a parse tree produced by the {@code showCountErrors}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void exitShowCountErrors(SpeakQlParser.ShowCountErrorsContext ctx);
	/**
	 * Enter a parse tree produced by the {@code showSchemaFilter}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void enterShowSchemaFilter(SpeakQlParser.ShowSchemaFilterContext ctx);
	/**
	 * Exit a parse tree produced by the {@code showSchemaFilter}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void exitShowSchemaFilter(SpeakQlParser.ShowSchemaFilterContext ctx);
	/**
	 * Enter a parse tree produced by the {@code showRoutine}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void enterShowRoutine(SpeakQlParser.ShowRoutineContext ctx);
	/**
	 * Exit a parse tree produced by the {@code showRoutine}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void exitShowRoutine(SpeakQlParser.ShowRoutineContext ctx);
	/**
	 * Enter a parse tree produced by the {@code showGrants}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void enterShowGrants(SpeakQlParser.ShowGrantsContext ctx);
	/**
	 * Exit a parse tree produced by the {@code showGrants}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void exitShowGrants(SpeakQlParser.ShowGrantsContext ctx);
	/**
	 * Enter a parse tree produced by the {@code showIndexes}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void enterShowIndexes(SpeakQlParser.ShowIndexesContext ctx);
	/**
	 * Exit a parse tree produced by the {@code showIndexes}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void exitShowIndexes(SpeakQlParser.ShowIndexesContext ctx);
	/**
	 * Enter a parse tree produced by the {@code showOpenTables}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void enterShowOpenTables(SpeakQlParser.ShowOpenTablesContext ctx);
	/**
	 * Exit a parse tree produced by the {@code showOpenTables}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void exitShowOpenTables(SpeakQlParser.ShowOpenTablesContext ctx);
	/**
	 * Enter a parse tree produced by the {@code showProfile}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void enterShowProfile(SpeakQlParser.ShowProfileContext ctx);
	/**
	 * Exit a parse tree produced by the {@code showProfile}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void exitShowProfile(SpeakQlParser.ShowProfileContext ctx);
	/**
	 * Enter a parse tree produced by the {@code showSlaveStatus}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void enterShowSlaveStatus(SpeakQlParser.ShowSlaveStatusContext ctx);
	/**
	 * Exit a parse tree produced by the {@code showSlaveStatus}
	 * labeled alternative in {@link SpeakQlParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void exitShowSlaveStatus(SpeakQlParser.ShowSlaveStatusContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#variableClause}.
	 * @param ctx the parse tree
	 */
	void enterVariableClause(SpeakQlParser.VariableClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#variableClause}.
	 * @param ctx the parse tree
	 */
	void exitVariableClause(SpeakQlParser.VariableClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#showCommonEntity}.
	 * @param ctx the parse tree
	 */
	void enterShowCommonEntity(SpeakQlParser.ShowCommonEntityContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#showCommonEntity}.
	 * @param ctx the parse tree
	 */
	void exitShowCommonEntity(SpeakQlParser.ShowCommonEntityContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#showFilter}.
	 * @param ctx the parse tree
	 */
	void enterShowFilter(SpeakQlParser.ShowFilterContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#showFilter}.
	 * @param ctx the parse tree
	 */
	void exitShowFilter(SpeakQlParser.ShowFilterContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#showGlobalInfoClause}.
	 * @param ctx the parse tree
	 */
	void enterShowGlobalInfoClause(SpeakQlParser.ShowGlobalInfoClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#showGlobalInfoClause}.
	 * @param ctx the parse tree
	 */
	void exitShowGlobalInfoClause(SpeakQlParser.ShowGlobalInfoClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#showSchemaEntity}.
	 * @param ctx the parse tree
	 */
	void enterShowSchemaEntity(SpeakQlParser.ShowSchemaEntityContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#showSchemaEntity}.
	 * @param ctx the parse tree
	 */
	void exitShowSchemaEntity(SpeakQlParser.ShowSchemaEntityContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#showProfileType}.
	 * @param ctx the parse tree
	 */
	void enterShowProfileType(SpeakQlParser.ShowProfileTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#showProfileType}.
	 * @param ctx the parse tree
	 */
	void exitShowProfileType(SpeakQlParser.ShowProfileTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#binlogStatement}.
	 * @param ctx the parse tree
	 */
	void enterBinlogStatement(SpeakQlParser.BinlogStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#binlogStatement}.
	 * @param ctx the parse tree
	 */
	void exitBinlogStatement(SpeakQlParser.BinlogStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#cacheIndexStatement}.
	 * @param ctx the parse tree
	 */
	void enterCacheIndexStatement(SpeakQlParser.CacheIndexStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#cacheIndexStatement}.
	 * @param ctx the parse tree
	 */
	void exitCacheIndexStatement(SpeakQlParser.CacheIndexStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#flushStatement}.
	 * @param ctx the parse tree
	 */
	void enterFlushStatement(SpeakQlParser.FlushStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#flushStatement}.
	 * @param ctx the parse tree
	 */
	void exitFlushStatement(SpeakQlParser.FlushStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#killStatement}.
	 * @param ctx the parse tree
	 */
	void enterKillStatement(SpeakQlParser.KillStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#killStatement}.
	 * @param ctx the parse tree
	 */
	void exitKillStatement(SpeakQlParser.KillStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#loadIndexIntoCache}.
	 * @param ctx the parse tree
	 */
	void enterLoadIndexIntoCache(SpeakQlParser.LoadIndexIntoCacheContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#loadIndexIntoCache}.
	 * @param ctx the parse tree
	 */
	void exitLoadIndexIntoCache(SpeakQlParser.LoadIndexIntoCacheContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#resetStatement}.
	 * @param ctx the parse tree
	 */
	void enterResetStatement(SpeakQlParser.ResetStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#resetStatement}.
	 * @param ctx the parse tree
	 */
	void exitResetStatement(SpeakQlParser.ResetStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#shutdownStatement}.
	 * @param ctx the parse tree
	 */
	void enterShutdownStatement(SpeakQlParser.ShutdownStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#shutdownStatement}.
	 * @param ctx the parse tree
	 */
	void exitShutdownStatement(SpeakQlParser.ShutdownStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#tableIndexes}.
	 * @param ctx the parse tree
	 */
	void enterTableIndexes(SpeakQlParser.TableIndexesContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#tableIndexes}.
	 * @param ctx the parse tree
	 */
	void exitTableIndexes(SpeakQlParser.TableIndexesContext ctx);
	/**
	 * Enter a parse tree produced by the {@code simpleFlushOption}
	 * labeled alternative in {@link SpeakQlParser#flushOption}.
	 * @param ctx the parse tree
	 */
	void enterSimpleFlushOption(SpeakQlParser.SimpleFlushOptionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code simpleFlushOption}
	 * labeled alternative in {@link SpeakQlParser#flushOption}.
	 * @param ctx the parse tree
	 */
	void exitSimpleFlushOption(SpeakQlParser.SimpleFlushOptionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code channelFlushOption}
	 * labeled alternative in {@link SpeakQlParser#flushOption}.
	 * @param ctx the parse tree
	 */
	void enterChannelFlushOption(SpeakQlParser.ChannelFlushOptionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code channelFlushOption}
	 * labeled alternative in {@link SpeakQlParser#flushOption}.
	 * @param ctx the parse tree
	 */
	void exitChannelFlushOption(SpeakQlParser.ChannelFlushOptionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tableFlushOption}
	 * labeled alternative in {@link SpeakQlParser#flushOption}.
	 * @param ctx the parse tree
	 */
	void enterTableFlushOption(SpeakQlParser.TableFlushOptionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tableFlushOption}
	 * labeled alternative in {@link SpeakQlParser#flushOption}.
	 * @param ctx the parse tree
	 */
	void exitTableFlushOption(SpeakQlParser.TableFlushOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#flushTableOption}.
	 * @param ctx the parse tree
	 */
	void enterFlushTableOption(SpeakQlParser.FlushTableOptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#flushTableOption}.
	 * @param ctx the parse tree
	 */
	void exitFlushTableOption(SpeakQlParser.FlushTableOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#loadedTableIndexes}.
	 * @param ctx the parse tree
	 */
	void enterLoadedTableIndexes(SpeakQlParser.LoadedTableIndexesContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#loadedTableIndexes}.
	 * @param ctx the parse tree
	 */
	void exitLoadedTableIndexes(SpeakQlParser.LoadedTableIndexesContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#simpleDescribeStatement}.
	 * @param ctx the parse tree
	 */
	void enterSimpleDescribeStatement(SpeakQlParser.SimpleDescribeStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#simpleDescribeStatement}.
	 * @param ctx the parse tree
	 */
	void exitSimpleDescribeStatement(SpeakQlParser.SimpleDescribeStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#fullDescribeStatement}.
	 * @param ctx the parse tree
	 */
	void enterFullDescribeStatement(SpeakQlParser.FullDescribeStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#fullDescribeStatement}.
	 * @param ctx the parse tree
	 */
	void exitFullDescribeStatement(SpeakQlParser.FullDescribeStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#helpStatement}.
	 * @param ctx the parse tree
	 */
	void enterHelpStatement(SpeakQlParser.HelpStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#helpStatement}.
	 * @param ctx the parse tree
	 */
	void exitHelpStatement(SpeakQlParser.HelpStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#useStatement}.
	 * @param ctx the parse tree
	 */
	void enterUseStatement(SpeakQlParser.UseStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#useStatement}.
	 * @param ctx the parse tree
	 */
	void exitUseStatement(SpeakQlParser.UseStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#signalStatement}.
	 * @param ctx the parse tree
	 */
	void enterSignalStatement(SpeakQlParser.SignalStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#signalStatement}.
	 * @param ctx the parse tree
	 */
	void exitSignalStatement(SpeakQlParser.SignalStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#resignalStatement}.
	 * @param ctx the parse tree
	 */
	void enterResignalStatement(SpeakQlParser.ResignalStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#resignalStatement}.
	 * @param ctx the parse tree
	 */
	void exitResignalStatement(SpeakQlParser.ResignalStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#signalConditionInformation}.
	 * @param ctx the parse tree
	 */
	void enterSignalConditionInformation(SpeakQlParser.SignalConditionInformationContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#signalConditionInformation}.
	 * @param ctx the parse tree
	 */
	void exitSignalConditionInformation(SpeakQlParser.SignalConditionInformationContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#diagnosticsStatement}.
	 * @param ctx the parse tree
	 */
	void enterDiagnosticsStatement(SpeakQlParser.DiagnosticsStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#diagnosticsStatement}.
	 * @param ctx the parse tree
	 */
	void exitDiagnosticsStatement(SpeakQlParser.DiagnosticsStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#diagnosticsConditionInformationName}.
	 * @param ctx the parse tree
	 */
	void enterDiagnosticsConditionInformationName(SpeakQlParser.DiagnosticsConditionInformationNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#diagnosticsConditionInformationName}.
	 * @param ctx the parse tree
	 */
	void exitDiagnosticsConditionInformationName(SpeakQlParser.DiagnosticsConditionInformationNameContext ctx);
	/**
	 * Enter a parse tree produced by the {@code describeStatements}
	 * labeled alternative in {@link SpeakQlParser#describeObjectClause}.
	 * @param ctx the parse tree
	 */
	void enterDescribeStatements(SpeakQlParser.DescribeStatementsContext ctx);
	/**
	 * Exit a parse tree produced by the {@code describeStatements}
	 * labeled alternative in {@link SpeakQlParser#describeObjectClause}.
	 * @param ctx the parse tree
	 */
	void exitDescribeStatements(SpeakQlParser.DescribeStatementsContext ctx);
	/**
	 * Enter a parse tree produced by the {@code describeConnection}
	 * labeled alternative in {@link SpeakQlParser#describeObjectClause}.
	 * @param ctx the parse tree
	 */
	void enterDescribeConnection(SpeakQlParser.DescribeConnectionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code describeConnection}
	 * labeled alternative in {@link SpeakQlParser#describeObjectClause}.
	 * @param ctx the parse tree
	 */
	void exitDescribeConnection(SpeakQlParser.DescribeConnectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#fullId}.
	 * @param ctx the parse tree
	 */
	void enterFullId(SpeakQlParser.FullIdContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#fullId}.
	 * @param ctx the parse tree
	 */
	void exitFullId(SpeakQlParser.FullIdContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#tableName}.
	 * @param ctx the parse tree
	 */
	void enterTableName(SpeakQlParser.TableNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#tableName}.
	 * @param ctx the parse tree
	 */
	void exitTableName(SpeakQlParser.TableNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#fullColumnName}.
	 * @param ctx the parse tree
	 */
	void enterFullColumnName(SpeakQlParser.FullColumnNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#fullColumnName}.
	 * @param ctx the parse tree
	 */
	void exitFullColumnName(SpeakQlParser.FullColumnNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#indexColumnName}.
	 * @param ctx the parse tree
	 */
	void enterIndexColumnName(SpeakQlParser.IndexColumnNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#indexColumnName}.
	 * @param ctx the parse tree
	 */
	void exitIndexColumnName(SpeakQlParser.IndexColumnNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#userName}.
	 * @param ctx the parse tree
	 */
	void enterUserName(SpeakQlParser.UserNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#userName}.
	 * @param ctx the parse tree
	 */
	void exitUserName(SpeakQlParser.UserNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#mysqlVariable}.
	 * @param ctx the parse tree
	 */
	void enterMysqlVariable(SpeakQlParser.MysqlVariableContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#mysqlVariable}.
	 * @param ctx the parse tree
	 */
	void exitMysqlVariable(SpeakQlParser.MysqlVariableContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#charsetName}.
	 * @param ctx the parse tree
	 */
	void enterCharsetName(SpeakQlParser.CharsetNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#charsetName}.
	 * @param ctx the parse tree
	 */
	void exitCharsetName(SpeakQlParser.CharsetNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#collationName}.
	 * @param ctx the parse tree
	 */
	void enterCollationName(SpeakQlParser.CollationNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#collationName}.
	 * @param ctx the parse tree
	 */
	void exitCollationName(SpeakQlParser.CollationNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#engineName}.
	 * @param ctx the parse tree
	 */
	void enterEngineName(SpeakQlParser.EngineNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#engineName}.
	 * @param ctx the parse tree
	 */
	void exitEngineName(SpeakQlParser.EngineNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#uuidSet}.
	 * @param ctx the parse tree
	 */
	void enterUuidSet(SpeakQlParser.UuidSetContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#uuidSet}.
	 * @param ctx the parse tree
	 */
	void exitUuidSet(SpeakQlParser.UuidSetContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#xid}.
	 * @param ctx the parse tree
	 */
	void enterXid(SpeakQlParser.XidContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#xid}.
	 * @param ctx the parse tree
	 */
	void exitXid(SpeakQlParser.XidContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#xuidStringId}.
	 * @param ctx the parse tree
	 */
	void enterXuidStringId(SpeakQlParser.XuidStringIdContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#xuidStringId}.
	 * @param ctx the parse tree
	 */
	void exitXuidStringId(SpeakQlParser.XuidStringIdContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#authPlugin}.
	 * @param ctx the parse tree
	 */
	void enterAuthPlugin(SpeakQlParser.AuthPluginContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#authPlugin}.
	 * @param ctx the parse tree
	 */
	void exitAuthPlugin(SpeakQlParser.AuthPluginContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#uid}.
	 * @param ctx the parse tree
	 */
	void enterUid(SpeakQlParser.UidContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#uid}.
	 * @param ctx the parse tree
	 */
	void exitUid(SpeakQlParser.UidContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#simpleId}.
	 * @param ctx the parse tree
	 */
	void enterSimpleId(SpeakQlParser.SimpleIdContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#simpleId}.
	 * @param ctx the parse tree
	 */
	void exitSimpleId(SpeakQlParser.SimpleIdContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#dottedId}.
	 * @param ctx the parse tree
	 */
	void enterDottedId(SpeakQlParser.DottedIdContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#dottedId}.
	 * @param ctx the parse tree
	 */
	void exitDottedId(SpeakQlParser.DottedIdContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#decimalLiteral}.
	 * @param ctx the parse tree
	 */
	void enterDecimalLiteral(SpeakQlParser.DecimalLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#decimalLiteral}.
	 * @param ctx the parse tree
	 */
	void exitDecimalLiteral(SpeakQlParser.DecimalLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#fileSizeLiteral}.
	 * @param ctx the parse tree
	 */
	void enterFileSizeLiteral(SpeakQlParser.FileSizeLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#fileSizeLiteral}.
	 * @param ctx the parse tree
	 */
	void exitFileSizeLiteral(SpeakQlParser.FileSizeLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#stringLiteral}.
	 * @param ctx the parse tree
	 */
	void enterStringLiteral(SpeakQlParser.StringLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#stringLiteral}.
	 * @param ctx the parse tree
	 */
	void exitStringLiteral(SpeakQlParser.StringLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#booleanLiteral}.
	 * @param ctx the parse tree
	 */
	void enterBooleanLiteral(SpeakQlParser.BooleanLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#booleanLiteral}.
	 * @param ctx the parse tree
	 */
	void exitBooleanLiteral(SpeakQlParser.BooleanLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#hexadecimalLiteral}.
	 * @param ctx the parse tree
	 */
	void enterHexadecimalLiteral(SpeakQlParser.HexadecimalLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#hexadecimalLiteral}.
	 * @param ctx the parse tree
	 */
	void exitHexadecimalLiteral(SpeakQlParser.HexadecimalLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#nullNotnull}.
	 * @param ctx the parse tree
	 */
	void enterNullNotnull(SpeakQlParser.NullNotnullContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#nullNotnull}.
	 * @param ctx the parse tree
	 */
	void exitNullNotnull(SpeakQlParser.NullNotnullContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#constant}.
	 * @param ctx the parse tree
	 */
	void enterConstant(SpeakQlParser.ConstantContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#constant}.
	 * @param ctx the parse tree
	 */
	void exitConstant(SpeakQlParser.ConstantContext ctx);
	/**
	 * Enter a parse tree produced by the {@code stringDataType}
	 * labeled alternative in {@link SpeakQlParser#dataType}.
	 * @param ctx the parse tree
	 */
	void enterStringDataType(SpeakQlParser.StringDataTypeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code stringDataType}
	 * labeled alternative in {@link SpeakQlParser#dataType}.
	 * @param ctx the parse tree
	 */
	void exitStringDataType(SpeakQlParser.StringDataTypeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code nationalStringDataType}
	 * labeled alternative in {@link SpeakQlParser#dataType}.
	 * @param ctx the parse tree
	 */
	void enterNationalStringDataType(SpeakQlParser.NationalStringDataTypeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code nationalStringDataType}
	 * labeled alternative in {@link SpeakQlParser#dataType}.
	 * @param ctx the parse tree
	 */
	void exitNationalStringDataType(SpeakQlParser.NationalStringDataTypeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code nationalVaryingStringDataType}
	 * labeled alternative in {@link SpeakQlParser#dataType}.
	 * @param ctx the parse tree
	 */
	void enterNationalVaryingStringDataType(SpeakQlParser.NationalVaryingStringDataTypeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code nationalVaryingStringDataType}
	 * labeled alternative in {@link SpeakQlParser#dataType}.
	 * @param ctx the parse tree
	 */
	void exitNationalVaryingStringDataType(SpeakQlParser.NationalVaryingStringDataTypeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code dimensionDataType}
	 * labeled alternative in {@link SpeakQlParser#dataType}.
	 * @param ctx the parse tree
	 */
	void enterDimensionDataType(SpeakQlParser.DimensionDataTypeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code dimensionDataType}
	 * labeled alternative in {@link SpeakQlParser#dataType}.
	 * @param ctx the parse tree
	 */
	void exitDimensionDataType(SpeakQlParser.DimensionDataTypeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code simpleDataType}
	 * labeled alternative in {@link SpeakQlParser#dataType}.
	 * @param ctx the parse tree
	 */
	void enterSimpleDataType(SpeakQlParser.SimpleDataTypeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code simpleDataType}
	 * labeled alternative in {@link SpeakQlParser#dataType}.
	 * @param ctx the parse tree
	 */
	void exitSimpleDataType(SpeakQlParser.SimpleDataTypeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code collectionDataType}
	 * labeled alternative in {@link SpeakQlParser#dataType}.
	 * @param ctx the parse tree
	 */
	void enterCollectionDataType(SpeakQlParser.CollectionDataTypeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code collectionDataType}
	 * labeled alternative in {@link SpeakQlParser#dataType}.
	 * @param ctx the parse tree
	 */
	void exitCollectionDataType(SpeakQlParser.CollectionDataTypeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code spatialDataType}
	 * labeled alternative in {@link SpeakQlParser#dataType}.
	 * @param ctx the parse tree
	 */
	void enterSpatialDataType(SpeakQlParser.SpatialDataTypeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code spatialDataType}
	 * labeled alternative in {@link SpeakQlParser#dataType}.
	 * @param ctx the parse tree
	 */
	void exitSpatialDataType(SpeakQlParser.SpatialDataTypeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code longVarcharDataType}
	 * labeled alternative in {@link SpeakQlParser#dataType}.
	 * @param ctx the parse tree
	 */
	void enterLongVarcharDataType(SpeakQlParser.LongVarcharDataTypeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code longVarcharDataType}
	 * labeled alternative in {@link SpeakQlParser#dataType}.
	 * @param ctx the parse tree
	 */
	void exitLongVarcharDataType(SpeakQlParser.LongVarcharDataTypeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code longVarbinaryDataType}
	 * labeled alternative in {@link SpeakQlParser#dataType}.
	 * @param ctx the parse tree
	 */
	void enterLongVarbinaryDataType(SpeakQlParser.LongVarbinaryDataTypeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code longVarbinaryDataType}
	 * labeled alternative in {@link SpeakQlParser#dataType}.
	 * @param ctx the parse tree
	 */
	void exitLongVarbinaryDataType(SpeakQlParser.LongVarbinaryDataTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#collectionOptions}.
	 * @param ctx the parse tree
	 */
	void enterCollectionOptions(SpeakQlParser.CollectionOptionsContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#collectionOptions}.
	 * @param ctx the parse tree
	 */
	void exitCollectionOptions(SpeakQlParser.CollectionOptionsContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#convertedDataType}.
	 * @param ctx the parse tree
	 */
	void enterConvertedDataType(SpeakQlParser.ConvertedDataTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#convertedDataType}.
	 * @param ctx the parse tree
	 */
	void exitConvertedDataType(SpeakQlParser.ConvertedDataTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#lengthOneDimension}.
	 * @param ctx the parse tree
	 */
	void enterLengthOneDimension(SpeakQlParser.LengthOneDimensionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#lengthOneDimension}.
	 * @param ctx the parse tree
	 */
	void exitLengthOneDimension(SpeakQlParser.LengthOneDimensionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#lengthTwoDimension}.
	 * @param ctx the parse tree
	 */
	void enterLengthTwoDimension(SpeakQlParser.LengthTwoDimensionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#lengthTwoDimension}.
	 * @param ctx the parse tree
	 */
	void exitLengthTwoDimension(SpeakQlParser.LengthTwoDimensionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#lengthTwoOptionalDimension}.
	 * @param ctx the parse tree
	 */
	void enterLengthTwoOptionalDimension(SpeakQlParser.LengthTwoOptionalDimensionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#lengthTwoOptionalDimension}.
	 * @param ctx the parse tree
	 */
	void exitLengthTwoOptionalDimension(SpeakQlParser.LengthTwoOptionalDimensionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#uidList}.
	 * @param ctx the parse tree
	 */
	void enterUidList(SpeakQlParser.UidListContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#uidList}.
	 * @param ctx the parse tree
	 */
	void exitUidList(SpeakQlParser.UidListContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#tables}.
	 * @param ctx the parse tree
	 */
	void enterTables(SpeakQlParser.TablesContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#tables}.
	 * @param ctx the parse tree
	 */
	void exitTables(SpeakQlParser.TablesContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#indexColumnNames}.
	 * @param ctx the parse tree
	 */
	void enterIndexColumnNames(SpeakQlParser.IndexColumnNamesContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#indexColumnNames}.
	 * @param ctx the parse tree
	 */
	void exitIndexColumnNames(SpeakQlParser.IndexColumnNamesContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#expressions}.
	 * @param ctx the parse tree
	 */
	void enterExpressions(SpeakQlParser.ExpressionsContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#expressions}.
	 * @param ctx the parse tree
	 */
	void exitExpressions(SpeakQlParser.ExpressionsContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#expressionsWithDefaults}.
	 * @param ctx the parse tree
	 */
	void enterExpressionsWithDefaults(SpeakQlParser.ExpressionsWithDefaultsContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#expressionsWithDefaults}.
	 * @param ctx the parse tree
	 */
	void exitExpressionsWithDefaults(SpeakQlParser.ExpressionsWithDefaultsContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#constants}.
	 * @param ctx the parse tree
	 */
	void enterConstants(SpeakQlParser.ConstantsContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#constants}.
	 * @param ctx the parse tree
	 */
	void exitConstants(SpeakQlParser.ConstantsContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#simpleStrings}.
	 * @param ctx the parse tree
	 */
	void enterSimpleStrings(SpeakQlParser.SimpleStringsContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#simpleStrings}.
	 * @param ctx the parse tree
	 */
	void exitSimpleStrings(SpeakQlParser.SimpleStringsContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#userVariables}.
	 * @param ctx the parse tree
	 */
	void enterUserVariables(SpeakQlParser.UserVariablesContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#userVariables}.
	 * @param ctx the parse tree
	 */
	void exitUserVariables(SpeakQlParser.UserVariablesContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#defaultValue}.
	 * @param ctx the parse tree
	 */
	void enterDefaultValue(SpeakQlParser.DefaultValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#defaultValue}.
	 * @param ctx the parse tree
	 */
	void exitDefaultValue(SpeakQlParser.DefaultValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#currentTimestamp}.
	 * @param ctx the parse tree
	 */
	void enterCurrentTimestamp(SpeakQlParser.CurrentTimestampContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#currentTimestamp}.
	 * @param ctx the parse tree
	 */
	void exitCurrentTimestamp(SpeakQlParser.CurrentTimestampContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#expressionOrDefault}.
	 * @param ctx the parse tree
	 */
	void enterExpressionOrDefault(SpeakQlParser.ExpressionOrDefaultContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#expressionOrDefault}.
	 * @param ctx the parse tree
	 */
	void exitExpressionOrDefault(SpeakQlParser.ExpressionOrDefaultContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#ifExists}.
	 * @param ctx the parse tree
	 */
	void enterIfExists(SpeakQlParser.IfExistsContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#ifExists}.
	 * @param ctx the parse tree
	 */
	void exitIfExists(SpeakQlParser.IfExistsContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#ifNotExists}.
	 * @param ctx the parse tree
	 */
	void enterIfNotExists(SpeakQlParser.IfNotExistsContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#ifNotExists}.
	 * @param ctx the parse tree
	 */
	void exitIfNotExists(SpeakQlParser.IfNotExistsContext ctx);
	/**
	 * Enter a parse tree produced by the {@code specificFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void enterSpecificFunctionCall(SpeakQlParser.SpecificFunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by the {@code specificFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void exitSpecificFunctionCall(SpeakQlParser.SpecificFunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by the {@code aggregateFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void enterAggregateFunctionCall(SpeakQlParser.AggregateFunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by the {@code aggregateFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void exitAggregateFunctionCall(SpeakQlParser.AggregateFunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by the {@code nonAggregateFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void enterNonAggregateFunctionCall(SpeakQlParser.NonAggregateFunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by the {@code nonAggregateFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void exitNonAggregateFunctionCall(SpeakQlParser.NonAggregateFunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by the {@code scalarFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void enterScalarFunctionCall(SpeakQlParser.ScalarFunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by the {@code scalarFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void exitScalarFunctionCall(SpeakQlParser.ScalarFunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by the {@code udfFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void enterUdfFunctionCall(SpeakQlParser.UdfFunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by the {@code udfFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void exitUdfFunctionCall(SpeakQlParser.UdfFunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by the {@code passwordFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void enterPasswordFunctionCall(SpeakQlParser.PasswordFunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by the {@code passwordFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void exitPasswordFunctionCall(SpeakQlParser.PasswordFunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by the {@code simpleFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 */
	void enterSimpleFunctionCall(SpeakQlParser.SimpleFunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by the {@code simpleFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 */
	void exitSimpleFunctionCall(SpeakQlParser.SimpleFunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by the {@code dataTypeFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 */
	void enterDataTypeFunctionCall(SpeakQlParser.DataTypeFunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by the {@code dataTypeFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 */
	void exitDataTypeFunctionCall(SpeakQlParser.DataTypeFunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by the {@code valuesFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 */
	void enterValuesFunctionCall(SpeakQlParser.ValuesFunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by the {@code valuesFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 */
	void exitValuesFunctionCall(SpeakQlParser.ValuesFunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by the {@code caseExpressionFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 */
	void enterCaseExpressionFunctionCall(SpeakQlParser.CaseExpressionFunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by the {@code caseExpressionFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 */
	void exitCaseExpressionFunctionCall(SpeakQlParser.CaseExpressionFunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by the {@code caseFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 */
	void enterCaseFunctionCall(SpeakQlParser.CaseFunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by the {@code caseFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 */
	void exitCaseFunctionCall(SpeakQlParser.CaseFunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by the {@code charFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 */
	void enterCharFunctionCall(SpeakQlParser.CharFunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by the {@code charFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 */
	void exitCharFunctionCall(SpeakQlParser.CharFunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by the {@code positionFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 */
	void enterPositionFunctionCall(SpeakQlParser.PositionFunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by the {@code positionFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 */
	void exitPositionFunctionCall(SpeakQlParser.PositionFunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by the {@code substrFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 */
	void enterSubstrFunctionCall(SpeakQlParser.SubstrFunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by the {@code substrFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 */
	void exitSubstrFunctionCall(SpeakQlParser.SubstrFunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by the {@code trimFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 */
	void enterTrimFunctionCall(SpeakQlParser.TrimFunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by the {@code trimFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 */
	void exitTrimFunctionCall(SpeakQlParser.TrimFunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by the {@code weightFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 */
	void enterWeightFunctionCall(SpeakQlParser.WeightFunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by the {@code weightFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 */
	void exitWeightFunctionCall(SpeakQlParser.WeightFunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by the {@code extractFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 */
	void enterExtractFunctionCall(SpeakQlParser.ExtractFunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by the {@code extractFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 */
	void exitExtractFunctionCall(SpeakQlParser.ExtractFunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by the {@code getFormatFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 */
	void enterGetFormatFunctionCall(SpeakQlParser.GetFormatFunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by the {@code getFormatFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 */
	void exitGetFormatFunctionCall(SpeakQlParser.GetFormatFunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by the {@code jsonValueFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 */
	void enterJsonValueFunctionCall(SpeakQlParser.JsonValueFunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by the {@code jsonValueFunctionCall}
	 * labeled alternative in {@link SpeakQlParser#specificFunction}.
	 * @param ctx the parse tree
	 */
	void exitJsonValueFunctionCall(SpeakQlParser.JsonValueFunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#caseFuncAlternative}.
	 * @param ctx the parse tree
	 */
	void enterCaseFuncAlternative(SpeakQlParser.CaseFuncAlternativeContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#caseFuncAlternative}.
	 * @param ctx the parse tree
	 */
	void exitCaseFuncAlternative(SpeakQlParser.CaseFuncAlternativeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code levelWeightList}
	 * labeled alternative in {@link SpeakQlParser#levelsInWeightString}.
	 * @param ctx the parse tree
	 */
	void enterLevelWeightList(SpeakQlParser.LevelWeightListContext ctx);
	/**
	 * Exit a parse tree produced by the {@code levelWeightList}
	 * labeled alternative in {@link SpeakQlParser#levelsInWeightString}.
	 * @param ctx the parse tree
	 */
	void exitLevelWeightList(SpeakQlParser.LevelWeightListContext ctx);
	/**
	 * Enter a parse tree produced by the {@code levelWeightRange}
	 * labeled alternative in {@link SpeakQlParser#levelsInWeightString}.
	 * @param ctx the parse tree
	 */
	void enterLevelWeightRange(SpeakQlParser.LevelWeightRangeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code levelWeightRange}
	 * labeled alternative in {@link SpeakQlParser#levelsInWeightString}.
	 * @param ctx the parse tree
	 */
	void exitLevelWeightRange(SpeakQlParser.LevelWeightRangeContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#levelInWeightListElement}.
	 * @param ctx the parse tree
	 */
	void enterLevelInWeightListElement(SpeakQlParser.LevelInWeightListElementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#levelInWeightListElement}.
	 * @param ctx the parse tree
	 */
	void exitLevelInWeightListElement(SpeakQlParser.LevelInWeightListElementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#aggregateWindowedFunction}.
	 * @param ctx the parse tree
	 */
	void enterAggregateWindowedFunction(SpeakQlParser.AggregateWindowedFunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#aggregateWindowedFunction}.
	 * @param ctx the parse tree
	 */
	void exitAggregateWindowedFunction(SpeakQlParser.AggregateWindowedFunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#nonAggregateWindowedFunction}.
	 * @param ctx the parse tree
	 */
	void enterNonAggregateWindowedFunction(SpeakQlParser.NonAggregateWindowedFunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#nonAggregateWindowedFunction}.
	 * @param ctx the parse tree
	 */
	void exitNonAggregateWindowedFunction(SpeakQlParser.NonAggregateWindowedFunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#overClause}.
	 * @param ctx the parse tree
	 */
	void enterOverClause(SpeakQlParser.OverClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#overClause}.
	 * @param ctx the parse tree
	 */
	void exitOverClause(SpeakQlParser.OverClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#windowSpec}.
	 * @param ctx the parse tree
	 */
	void enterWindowSpec(SpeakQlParser.WindowSpecContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#windowSpec}.
	 * @param ctx the parse tree
	 */
	void exitWindowSpec(SpeakQlParser.WindowSpecContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#windowName}.
	 * @param ctx the parse tree
	 */
	void enterWindowName(SpeakQlParser.WindowNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#windowName}.
	 * @param ctx the parse tree
	 */
	void exitWindowName(SpeakQlParser.WindowNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#frameClause}.
	 * @param ctx the parse tree
	 */
	void enterFrameClause(SpeakQlParser.FrameClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#frameClause}.
	 * @param ctx the parse tree
	 */
	void exitFrameClause(SpeakQlParser.FrameClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#frameUnits}.
	 * @param ctx the parse tree
	 */
	void enterFrameUnits(SpeakQlParser.FrameUnitsContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#frameUnits}.
	 * @param ctx the parse tree
	 */
	void exitFrameUnits(SpeakQlParser.FrameUnitsContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#frameExtent}.
	 * @param ctx the parse tree
	 */
	void enterFrameExtent(SpeakQlParser.FrameExtentContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#frameExtent}.
	 * @param ctx the parse tree
	 */
	void exitFrameExtent(SpeakQlParser.FrameExtentContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#frameBetween}.
	 * @param ctx the parse tree
	 */
	void enterFrameBetween(SpeakQlParser.FrameBetweenContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#frameBetween}.
	 * @param ctx the parse tree
	 */
	void exitFrameBetween(SpeakQlParser.FrameBetweenContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#frameRange}.
	 * @param ctx the parse tree
	 */
	void enterFrameRange(SpeakQlParser.FrameRangeContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#frameRange}.
	 * @param ctx the parse tree
	 */
	void exitFrameRange(SpeakQlParser.FrameRangeContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#partitionClause}.
	 * @param ctx the parse tree
	 */
	void enterPartitionClause(SpeakQlParser.PartitionClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#partitionClause}.
	 * @param ctx the parse tree
	 */
	void exitPartitionClause(SpeakQlParser.PartitionClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#scalarFunctionName}.
	 * @param ctx the parse tree
	 */
	void enterScalarFunctionName(SpeakQlParser.ScalarFunctionNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#scalarFunctionName}.
	 * @param ctx the parse tree
	 */
	void exitScalarFunctionName(SpeakQlParser.ScalarFunctionNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#passwordFunctionClause}.
	 * @param ctx the parse tree
	 */
	void enterPasswordFunctionClause(SpeakQlParser.PasswordFunctionClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#passwordFunctionClause}.
	 * @param ctx the parse tree
	 */
	void exitPasswordFunctionClause(SpeakQlParser.PasswordFunctionClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#functionArgs}.
	 * @param ctx the parse tree
	 */
	void enterFunctionArgs(SpeakQlParser.FunctionArgsContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#functionArgs}.
	 * @param ctx the parse tree
	 */
	void exitFunctionArgs(SpeakQlParser.FunctionArgsContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#functionArg}.
	 * @param ctx the parse tree
	 */
	void enterFunctionArg(SpeakQlParser.FunctionArgContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#functionArg}.
	 * @param ctx the parse tree
	 */
	void exitFunctionArg(SpeakQlParser.FunctionArgContext ctx);
	/**
	 * Enter a parse tree produced by the {@code isExpression}
	 * labeled alternative in {@link SpeakQlParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterIsExpression(SpeakQlParser.IsExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code isExpression}
	 * labeled alternative in {@link SpeakQlParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitIsExpression(SpeakQlParser.IsExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code notExpression}
	 * labeled alternative in {@link SpeakQlParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterNotExpression(SpeakQlParser.NotExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code notExpression}
	 * labeled alternative in {@link SpeakQlParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitNotExpression(SpeakQlParser.NotExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code logicalExpression}
	 * labeled alternative in {@link SpeakQlParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterLogicalExpression(SpeakQlParser.LogicalExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code logicalExpression}
	 * labeled alternative in {@link SpeakQlParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitLogicalExpression(SpeakQlParser.LogicalExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code predicateExpression}
	 * labeled alternative in {@link SpeakQlParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterPredicateExpression(SpeakQlParser.PredicateExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code predicateExpression}
	 * labeled alternative in {@link SpeakQlParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitPredicateExpression(SpeakQlParser.PredicateExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code soundsLikePredicate}
	 * labeled alternative in {@link SpeakQlParser#predicate}.
	 * @param ctx the parse tree
	 */
	void enterSoundsLikePredicate(SpeakQlParser.SoundsLikePredicateContext ctx);
	/**
	 * Exit a parse tree produced by the {@code soundsLikePredicate}
	 * labeled alternative in {@link SpeakQlParser#predicate}.
	 * @param ctx the parse tree
	 */
	void exitSoundsLikePredicate(SpeakQlParser.SoundsLikePredicateContext ctx);
	/**
	 * Enter a parse tree produced by the {@code expressionAtomPredicate}
	 * labeled alternative in {@link SpeakQlParser#predicate}.
	 * @param ctx the parse tree
	 */
	void enterExpressionAtomPredicate(SpeakQlParser.ExpressionAtomPredicateContext ctx);
	/**
	 * Exit a parse tree produced by the {@code expressionAtomPredicate}
	 * labeled alternative in {@link SpeakQlParser#predicate}.
	 * @param ctx the parse tree
	 */
	void exitExpressionAtomPredicate(SpeakQlParser.ExpressionAtomPredicateContext ctx);
	/**
	 * Enter a parse tree produced by the {@code subqueryComparisonPredicate}
	 * labeled alternative in {@link SpeakQlParser#predicate}.
	 * @param ctx the parse tree
	 */
	void enterSubqueryComparisonPredicate(SpeakQlParser.SubqueryComparisonPredicateContext ctx);
	/**
	 * Exit a parse tree produced by the {@code subqueryComparisonPredicate}
	 * labeled alternative in {@link SpeakQlParser#predicate}.
	 * @param ctx the parse tree
	 */
	void exitSubqueryComparisonPredicate(SpeakQlParser.SubqueryComparisonPredicateContext ctx);
	/**
	 * Enter a parse tree produced by the {@code jsonMemberOfPredicate}
	 * labeled alternative in {@link SpeakQlParser#predicate}.
	 * @param ctx the parse tree
	 */
	void enterJsonMemberOfPredicate(SpeakQlParser.JsonMemberOfPredicateContext ctx);
	/**
	 * Exit a parse tree produced by the {@code jsonMemberOfPredicate}
	 * labeled alternative in {@link SpeakQlParser#predicate}.
	 * @param ctx the parse tree
	 */
	void exitJsonMemberOfPredicate(SpeakQlParser.JsonMemberOfPredicateContext ctx);
	/**
	 * Enter a parse tree produced by the {@code binaryComparisonPredicate}
	 * labeled alternative in {@link SpeakQlParser#predicate}.
	 * @param ctx the parse tree
	 */
	void enterBinaryComparisonPredicate(SpeakQlParser.BinaryComparisonPredicateContext ctx);
	/**
	 * Exit a parse tree produced by the {@code binaryComparisonPredicate}
	 * labeled alternative in {@link SpeakQlParser#predicate}.
	 * @param ctx the parse tree
	 */
	void exitBinaryComparisonPredicate(SpeakQlParser.BinaryComparisonPredicateContext ctx);
	/**
	 * Enter a parse tree produced by the {@code inPredicate}
	 * labeled alternative in {@link SpeakQlParser#predicate}.
	 * @param ctx the parse tree
	 */
	void enterInPredicate(SpeakQlParser.InPredicateContext ctx);
	/**
	 * Exit a parse tree produced by the {@code inPredicate}
	 * labeled alternative in {@link SpeakQlParser#predicate}.
	 * @param ctx the parse tree
	 */
	void exitInPredicate(SpeakQlParser.InPredicateContext ctx);
	/**
	 * Enter a parse tree produced by the {@code betweenPredicate}
	 * labeled alternative in {@link SpeakQlParser#predicate}.
	 * @param ctx the parse tree
	 */
	void enterBetweenPredicate(SpeakQlParser.BetweenPredicateContext ctx);
	/**
	 * Exit a parse tree produced by the {@code betweenPredicate}
	 * labeled alternative in {@link SpeakQlParser#predicate}.
	 * @param ctx the parse tree
	 */
	void exitBetweenPredicate(SpeakQlParser.BetweenPredicateContext ctx);
	/**
	 * Enter a parse tree produced by the {@code isNullPredicate}
	 * labeled alternative in {@link SpeakQlParser#predicate}.
	 * @param ctx the parse tree
	 */
	void enterIsNullPredicate(SpeakQlParser.IsNullPredicateContext ctx);
	/**
	 * Exit a parse tree produced by the {@code isNullPredicate}
	 * labeled alternative in {@link SpeakQlParser#predicate}.
	 * @param ctx the parse tree
	 */
	void exitIsNullPredicate(SpeakQlParser.IsNullPredicateContext ctx);
	/**
	 * Enter a parse tree produced by the {@code likePredicate}
	 * labeled alternative in {@link SpeakQlParser#predicate}.
	 * @param ctx the parse tree
	 */
	void enterLikePredicate(SpeakQlParser.LikePredicateContext ctx);
	/**
	 * Exit a parse tree produced by the {@code likePredicate}
	 * labeled alternative in {@link SpeakQlParser#predicate}.
	 * @param ctx the parse tree
	 */
	void exitLikePredicate(SpeakQlParser.LikePredicateContext ctx);
	/**
	 * Enter a parse tree produced by the {@code regexpPredicate}
	 * labeled alternative in {@link SpeakQlParser#predicate}.
	 * @param ctx the parse tree
	 */
	void enterRegexpPredicate(SpeakQlParser.RegexpPredicateContext ctx);
	/**
	 * Exit a parse tree produced by the {@code regexpPredicate}
	 * labeled alternative in {@link SpeakQlParser#predicate}.
	 * @param ctx the parse tree
	 */
	void exitRegexpPredicate(SpeakQlParser.RegexpPredicateContext ctx);
	/**
	 * Enter a parse tree produced by the {@code unaryExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 */
	void enterUnaryExpressionAtom(SpeakQlParser.UnaryExpressionAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code unaryExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 */
	void exitUnaryExpressionAtom(SpeakQlParser.UnaryExpressionAtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code collateExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 */
	void enterCollateExpressionAtom(SpeakQlParser.CollateExpressionAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code collateExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 */
	void exitCollateExpressionAtom(SpeakQlParser.CollateExpressionAtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code mysqlVariableExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 */
	void enterMysqlVariableExpressionAtom(SpeakQlParser.MysqlVariableExpressionAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code mysqlVariableExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 */
	void exitMysqlVariableExpressionAtom(SpeakQlParser.MysqlVariableExpressionAtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code nestedExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 */
	void enterNestedExpressionAtom(SpeakQlParser.NestedExpressionAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code nestedExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 */
	void exitNestedExpressionAtom(SpeakQlParser.NestedExpressionAtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code nestedRowExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 */
	void enterNestedRowExpressionAtom(SpeakQlParser.NestedRowExpressionAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code nestedRowExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 */
	void exitNestedRowExpressionAtom(SpeakQlParser.NestedRowExpressionAtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code mathExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 */
	void enterMathExpressionAtom(SpeakQlParser.MathExpressionAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code mathExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 */
	void exitMathExpressionAtom(SpeakQlParser.MathExpressionAtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code existsExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 */
	void enterExistsExpressionAtom(SpeakQlParser.ExistsExpressionAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code existsExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 */
	void exitExistsExpressionAtom(SpeakQlParser.ExistsExpressionAtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code intervalExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 */
	void enterIntervalExpressionAtom(SpeakQlParser.IntervalExpressionAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code intervalExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 */
	void exitIntervalExpressionAtom(SpeakQlParser.IntervalExpressionAtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code jsonExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 */
	void enterJsonExpressionAtom(SpeakQlParser.JsonExpressionAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code jsonExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 */
	void exitJsonExpressionAtom(SpeakQlParser.JsonExpressionAtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code subqueryExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 */
	void enterSubqueryExpressionAtom(SpeakQlParser.SubqueryExpressionAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code subqueryExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 */
	void exitSubqueryExpressionAtom(SpeakQlParser.SubqueryExpressionAtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code constantExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 */
	void enterConstantExpressionAtom(SpeakQlParser.ConstantExpressionAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code constantExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 */
	void exitConstantExpressionAtom(SpeakQlParser.ConstantExpressionAtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code functionCallExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCallExpressionAtom(SpeakQlParser.FunctionCallExpressionAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code functionCallExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCallExpressionAtom(SpeakQlParser.FunctionCallExpressionAtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code binaryExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 */
	void enterBinaryExpressionAtom(SpeakQlParser.BinaryExpressionAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code binaryExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 */
	void exitBinaryExpressionAtom(SpeakQlParser.BinaryExpressionAtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code fullColumnNameExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 */
	void enterFullColumnNameExpressionAtom(SpeakQlParser.FullColumnNameExpressionAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code fullColumnNameExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 */
	void exitFullColumnNameExpressionAtom(SpeakQlParser.FullColumnNameExpressionAtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code bitExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 */
	void enterBitExpressionAtom(SpeakQlParser.BitExpressionAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code bitExpressionAtom}
	 * labeled alternative in {@link SpeakQlParser#expressionAtom}.
	 * @param ctx the parse tree
	 */
	void exitBitExpressionAtom(SpeakQlParser.BitExpressionAtomContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#unaryOperator}.
	 * @param ctx the parse tree
	 */
	void enterUnaryOperator(SpeakQlParser.UnaryOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#unaryOperator}.
	 * @param ctx the parse tree
	 */
	void exitUnaryOperator(SpeakQlParser.UnaryOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#comparisonOperator}.
	 * @param ctx the parse tree
	 */
	void enterComparisonOperator(SpeakQlParser.ComparisonOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#comparisonOperator}.
	 * @param ctx the parse tree
	 */
	void exitComparisonOperator(SpeakQlParser.ComparisonOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#logicalOperator}.
	 * @param ctx the parse tree
	 */
	void enterLogicalOperator(SpeakQlParser.LogicalOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#logicalOperator}.
	 * @param ctx the parse tree
	 */
	void exitLogicalOperator(SpeakQlParser.LogicalOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#bitOperator}.
	 * @param ctx the parse tree
	 */
	void enterBitOperator(SpeakQlParser.BitOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#bitOperator}.
	 * @param ctx the parse tree
	 */
	void exitBitOperator(SpeakQlParser.BitOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#mathOperator}.
	 * @param ctx the parse tree
	 */
	void enterMathOperator(SpeakQlParser.MathOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#mathOperator}.
	 * @param ctx the parse tree
	 */
	void exitMathOperator(SpeakQlParser.MathOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#jsonOperator}.
	 * @param ctx the parse tree
	 */
	void enterJsonOperator(SpeakQlParser.JsonOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#jsonOperator}.
	 * @param ctx the parse tree
	 */
	void exitJsonOperator(SpeakQlParser.JsonOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#charsetNameBase}.
	 * @param ctx the parse tree
	 */
	void enterCharsetNameBase(SpeakQlParser.CharsetNameBaseContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#charsetNameBase}.
	 * @param ctx the parse tree
	 */
	void exitCharsetNameBase(SpeakQlParser.CharsetNameBaseContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#transactionLevelBase}.
	 * @param ctx the parse tree
	 */
	void enterTransactionLevelBase(SpeakQlParser.TransactionLevelBaseContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#transactionLevelBase}.
	 * @param ctx the parse tree
	 */
	void exitTransactionLevelBase(SpeakQlParser.TransactionLevelBaseContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#privilegesBase}.
	 * @param ctx the parse tree
	 */
	void enterPrivilegesBase(SpeakQlParser.PrivilegesBaseContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#privilegesBase}.
	 * @param ctx the parse tree
	 */
	void exitPrivilegesBase(SpeakQlParser.PrivilegesBaseContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#intervalTypeBase}.
	 * @param ctx the parse tree
	 */
	void enterIntervalTypeBase(SpeakQlParser.IntervalTypeBaseContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#intervalTypeBase}.
	 * @param ctx the parse tree
	 */
	void exitIntervalTypeBase(SpeakQlParser.IntervalTypeBaseContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#dataTypeBase}.
	 * @param ctx the parse tree
	 */
	void enterDataTypeBase(SpeakQlParser.DataTypeBaseContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#dataTypeBase}.
	 * @param ctx the parse tree
	 */
	void exitDataTypeBase(SpeakQlParser.DataTypeBaseContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#keywordsCanBeId}.
	 * @param ctx the parse tree
	 */
	void enterKeywordsCanBeId(SpeakQlParser.KeywordsCanBeIdContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#keywordsCanBeId}.
	 * @param ctx the parse tree
	 */
	void exitKeywordsCanBeId(SpeakQlParser.KeywordsCanBeIdContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpeakQlParser#functionNameBase}.
	 * @param ctx the parse tree
	 */
	void enterFunctionNameBase(SpeakQlParser.FunctionNameBaseContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpeakQlParser#functionNameBase}.
	 * @param ctx the parse tree
	 */
	void exitFunctionNameBase(SpeakQlParser.FunctionNameBaseContext ctx);
}
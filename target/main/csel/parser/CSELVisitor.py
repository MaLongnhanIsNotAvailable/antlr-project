# Generated from main/csel/parser/CSEL.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CSELParser import CSELParser
else:
    from CSELParser import CSELParser

# This class defines a complete generic visitor for a parse tree produced by CSELParser.

class CSELVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSELParser#program.
    def visitProgram(self, ctx:CSELParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#statements.
    def visitStatements(self, ctx:CSELParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#var_dec.
    def visitVar_dec(self, ctx:CSELParser.Var_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#arr_dec.
    def visitArr_dec(self, ctx:CSELParser.Arr_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#const_dec.
    def visitConst_dec(self, ctx:CSELParser.Const_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#const_arr_dec.
    def visitConst_arr_dec(self, ctx:CSELParser.Const_arr_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#assignment.
    def visitAssignment(self, ctx:CSELParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#if_statement.
    def visitIf_statement(self, ctx:CSELParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#for_statement.
    def visitFor_statement(self, ctx:CSELParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#while_statement.
    def visitWhile_statement(self, ctx:CSELParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#fun_dec.
    def visitFun_dec(self, ctx:CSELParser.Fun_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#params.
    def visitParams(self, ctx:CSELParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp.
    def visitExp(self, ctx:CSELParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp1.
    def visitExp1(self, ctx:CSELParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp2.
    def visitExp2(self, ctx:CSELParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp3.
    def visitExp3(self, ctx:CSELParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp4.
    def visitExp4(self, ctx:CSELParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp5.
    def visitExp5(self, ctx:CSELParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp6.
    def visitExp6(self, ctx:CSELParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp7.
    def visitExp7(self, ctx:CSELParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp8.
    def visitExp8(self, ctx:CSELParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp9.
    def visitExp9(self, ctx:CSELParser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#key_words.
    def visitKey_words(self, ctx:CSELParser.Key_wordsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#index_operators.
    def visitIndex_operators(self, ctx:CSELParser.Index_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#index_operand.
    def visitIndex_operand(self, ctx:CSELParser.Index_operandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#key_operators.
    def visitKey_operators(self, ctx:CSELParser.Key_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#key_operand.
    def visitKey_operand(self, ctx:CSELParser.Key_operandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#call_statement.
    def visitCall_statement(self, ctx:CSELParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#arr_lit.
    def visitArr_lit(self, ctx:CSELParser.Arr_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#arr_element.
    def visitArr_element(self, ctx:CSELParser.Arr_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#json_lit.
    def visitJson_lit(self, ctx:CSELParser.Json_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#json_element.
    def visitJson_element(self, ctx:CSELParser.Json_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#id_arr.
    def visitId_arr(self, ctx:CSELParser.Id_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#id_arr_const.
    def visitId_arr_const(self, ctx:CSELParser.Id_arr_constContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#num_lit.
    def visitNum_lit(self, ctx:CSELParser.Num_litContext):
        return self.visitChildren(ctx)



del CSELParser
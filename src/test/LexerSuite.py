import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
   
    ## ID
    def test_identifiers_case1(self):
        self.assertTrue(TestLexer.checkLexeme("philong","philong,<EOF>",101))
    def test_identifiers_case2(self):
        self.assertTrue(TestLexer.checkLexeme("$philong","$philong,<EOF>",102))
    def test_identifiers_case983(self):
        self.assertTrue(TestLexer.checkLexeme("$ABC philong","$ABC,philong,<EOF>",103))
    def test_identifiers_case4(self):
        self.assertTrue(TestLexer.checkLexeme("$aA_1 a123","$aA_1,a123,<EOF>",104))
    def test_identifiers_case5(self):
        self.assertTrue(TestLexer.checkLexeme("a123","a123,<EOF>",105))
    def test_identifiers_case6(self):
        self.assertTrue(TestLexer.checkLexeme("Abc","Error Token A",106))
    def test_identifiers_case7(self):
        self.assertTrue(TestLexer.checkLexeme("_Abc","Error Token _",107))
    def test_identifiers_case8(self):
        self.assertTrue(TestLexer.checkLexeme("1philong 123","1,philong,123,<EOF>",108)) #############################
    def test_identifiers_case9(self):   
        self.assertTrue(TestLexer.checkLexeme("philong?svn","philong,Error Token ?",109))
    def test_identifiers_case10(self):
        self.assertTrue(TestLexer.checkLexeme("_","Error Token _",110))
    
    # KEYS & OPERS & SEPORATORS 

    def test_key_words_case1(self):
        self.assertTrue(TestLexer.checkLexeme("ForOfInTrueFalseCallReturnNumber","For,Of,In,True,False,Call,Return,Number,<EOF>",111))
    def test_key_words_case2(self):
        self.assertTrue(TestLexer.checkLexeme("While For","While,For,<EOF>",112))
    def test_key_words_case983(self):
        self.assertTrue(TestLexer.checkLexeme("If Elif JSON","If,Elif,JSON,<EOF>",113))
    def test_key_words_case4(self):
        self.assertTrue(TestLexer.checkLexeme("Continue Of","Continue,Of,<EOF>",114))
    def test_key_words_case5(self):
        self.assertTrue(TestLexer.checkLexeme("True False boolean","True,False,boolean,<EOF>",115))
    def test_key_words_case6(self):                                        
        self.assertTrue(TestLexer.checkLexeme("String Let Constant","String,Let,Constant,<EOF>",116))
    def test_key_words_case7(self):
        self.assertTrue(TestLexer.checkLexeme("BreaK","Error Token B",117))
    def test_key_words_case8(self):
        self.assertTrue(TestLexer.checkLexeme("AND","Error Token A",118))
    def test_key_words_case9(self):
        self.assertTrue(TestLexer.checkLexeme("Json","Error Token J",119))
    def test_key_words_case10(self):
        self.assertTrue(TestLexer.checkLexeme("ArrAy","Error Token A",120))
   
    ## OPERS
    def test_operators_case1(self):
        self.assertTrue(TestLexer.checkLexeme("philong<>","philong,<,>,<EOF>",131))
    def test_operators_case2(self):
        self.assertTrue(TestLexer.checkLexeme("+-*/","+,-,*,/,<EOF>",132))
    def test_operators_case983(self):
        self.assertTrue(TestLexer.checkLexeme("a<b","a,<,b,<EOF>",133))
    def test_operators_case4(self):
        self.assertTrue(TestLexer.checkLexeme(">= <==>",">=,<=,=,>,<EOF>",134))
    def test_operators_case5(self):
        self.assertTrue(TestLexer.checkLexeme("&&","&&,<EOF>",135))
    def test_operators_case6(self):
        self.assertTrue(TestLexer.checkLexeme("||","||,<EOF>",136))
    def test_operators_case7(self):
        self.assertTrue(TestLexer.checkLexeme("== !!= =====","==,!,!=,==,==,=,<EOF>",137))
    def test_operators_case8(self):
        self.assertTrue(TestLexer.checkLexeme("=or<=<><>=-<=>","=,or,<=,<,>,<,>=,-,<=,>,<EOF>",138))
    def test_operators_case9(self):
        self.assertTrue(TestLexer.checkLexeme("not<>=and>=mod<=-and","not,<,>=,and,>=,mod,<=,-,and,<EOF>",139))
    def test_operators_case10(self):                                     
        self.assertTrue(TestLexer.checkLexeme("% %","%,%,<EOF>",140))
   
    ## NUMBER
    def test_number_case1(self):
        self.assertTrue(TestLexer.checkLexeme("5","5,<EOF>",161))
    def test_number_case2(self):
        self.assertTrue(TestLexer.checkLexeme("123.888","123.888,<EOF>",162))
    def test_number_case983(self):
        self.assertTrue(TestLexer.checkLexeme("12.3e983","12.3e983,<EOF>",163))
    def test_number_case4(self):
        self.assertTrue(TestLexer.checkLexeme("-12e983","-,12e983,<EOF>",164))
    def test_number_case5(self):
        self.assertTrue(TestLexer.checkLexeme("-123.4e-12","-,123.4e-12,<EOF>",165))
    def test_number_case6(self):
        self.assertTrue(TestLexer.checkLexeme("12.3e-30","12.3e-30,<EOF>",166))
    def test_number_case7(self):
        self.assertTrue(TestLexer.checkLexeme("12.","12.,<EOF>",167))
    def test_number_case8(self):
        self.assertTrue(TestLexer.checkLexeme(".4e-12",".,4e-12,<EOF>",168))
    def test_number_case9(self):
        self.assertTrue(TestLexer.checkLexeme("12.3e983.0","12.3e983,.,0,<EOF>",169))
    def test_number_case10(self):
        self.assertTrue(TestLexer.checkLexeme("e123","e123,<EOF>",170))
    
    
    ## STRING
    def test_string_case1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "philong"  ""","""philong,<EOF>""",121))
    def test_string_case2(self):
        self.assertTrue(TestLexer.checkLexeme("\"Abc123_*/-+*&^%!@#\"","Abc123_*/-+*&^%!@#,<EOF>",122))
    def test_string_case983(self):                                             
        self.assertTrue(TestLexer.checkLexeme("\"philong \\b \\f \\r \\n \\t  \\' ' \\\\ \"","philong \\b \\f \\r \\n \\t  \\' ' \\\\ ,<EOF>",123))
    def test_string_case4(self):
        self.assertTrue(TestLexer.checkLexeme("\"philong \\\\ '\" \"","philong \\\\ '\" ,<EOF>",124))
    def test_string_case5(self):
        self.assertTrue(TestLexer.checkLexeme("\"\"",",<EOF>",125))
    def test_string_case6(self):
        self.assertTrue(TestLexer.checkLexeme("philong \"'\"philong'\"\" ","philong,'\"philong'\",<EOF>",126))
    def test_string_case7(self):
        self.assertTrue(TestLexer.checkLexeme("\"philong","Unclosed String: philong",127))
    def test_string_case8(self):
        self.assertTrue(TestLexer.checkLexeme("\" '\" '\""," '\" ',<EOF>",128))
    def test_string_case9(self):
        self.assertTrue(TestLexer.checkLexeme("\"philong \\t \\h bcd\"","Illegal Escape In String: philong \\t \\h",129))
    def test_string_case10(self):
        self.assertTrue(TestLexer.checkLexeme("\" philong \\ philong \"","Illegal Escape In String:  philong \ ",130))
    ## ESCAPE
    def test_escape_case1(self):
        self.assertTrue(TestLexer.checkLexeme("\"bnhan\\ma\"","Illegal Escape In String: bnhan\\m",141))
    def test_escape_case2(self):
        self.assertTrue(TestLexer.checkLexeme("\"laMD\\HLSc\\na\"","Illegal Escape In String: laMD\\H",142))
    def test_escape_case983(self): 
        self.assertTrue(TestLexer.checkLexeme("\",dls\\F12!LS\\kc\\na\"","Illegal Escape In String: ,dls\\F",143))
    def test_escape_case4(self):
        self.assertTrue(TestLexer.checkLexeme("\"ado\\mado\"","Illegal Escape In String: ado\\m",144))
    def test_escape_case5(self):
        self.assertTrue(TestLexer.checkLexeme("123philong \"xyz\\k 888","123,philong,Illegal Escape In String: xyz\\k",145))
    def test_escape_case6(self):
        self.assertTrue(TestLexer.checkLexeme("\"aa\\wb\"","Illegal Escape In String: aa\\w",146))
    def test_escape_case7(self):
        self.assertTrue(TestLexer.checkLexeme("la+12+\"na\"\"md+1.2-468\lb","la,+,12,+,na,Illegal Escape In String: md+1.2-468\l",147))
    def test_escape_case8(self):
        self.assertTrue(TestLexer.checkLexeme("\"1.2+1.3+1.4\\o'\"123","Illegal Escape In String: 1.2+1.3+1.4\\o",148))
    def test_escape_case9(self):
        self.assertTrue(TestLexer.checkLexeme("+123\"la\\qm\f\"","+,123,Illegal Escape In String: la\\q",149))
    def test_escape_case10(self):
        self.assertTrue(TestLexer.checkLexeme("\"gimaha\\uabc","Illegal Escape In String: gimaha\\u",150))
    #Unclose STR
    def test_close_string_case1(self):
        self.assertTrue(TestLexer.checkLexeme("\"bnhanxyc","Unclosed String: bnhanxyc",151))
    def test_close_string_case2(self):
        self.assertTrue(TestLexer.checkLexeme("philong+\"`YS2h.J(","philong,+,Unclosed String: `YS2h.J(",152))
    def test_close_string_case983(self):
        self.assertTrue(TestLexer.checkLexeme("\"nhannv \" \"philong","nhannv ,Unclosed String: philong",153))
    def test_close_string_case4(self):
        self.assertTrue(TestLexer.checkLexeme("\"nhanms!,lds \"  123\"philong","nhanms!,lds ,123,Unclosed String: philong",154))
    def test_close_string_case5(self):
        self.assertTrue(TestLexer.checkLexeme("a+11.2+\"mam.123\" 12 \"%^&","a,+,11.2,+,mam.123,12,Unclosed String: %^&",155))
    def test_close_string_case6(self):
        self.assertTrue(TestLexer.checkLexeme("38n\"[#Ffs?0ED\"0.\"T`#!7n","38,n,[#Ffs?0ED,0.,Unclosed String: T`#!7n",156))
    def test_close_string_case7(self):
        self.assertTrue(TestLexer.checkLexeme("\".Hub`22Y\"<\"Y`=DxXhZKh",".Hub`22Y,<,Unclosed String: Y`=DxXhZKh",157))
    def test_close_string_case8(self):
        self.assertTrue(TestLexer.checkLexeme("\"ULxM*`~.~+C_DISD2","Unclosed String: ULxM*`~.~+C_DISD2",158))
    def test_close_string_case9(self):
        self.assertTrue(TestLexer.checkLexeme("\"Nk8U;\"rA\"@Y3*\"oV\"bh1","Nk8U;,rA,@Y3*,oV,Unclosed String: bh1",159))
    def test_close_string_case10(self):
        self.assertTrue(TestLexer.checkLexeme("\"o|F&)LqX\"+>+\"#Fft","o|F&)LqX,+,>,+,Unclosed String: #Fft",160))

    ##Comment:
    def test_comment_case1(self):
        self.assertTrue(TestLexer.checkLexeme("## philong ##","<EOF>",171))
    def test_comment_case2(self):
        self.assertTrue(TestLexer.checkLexeme("## 123#%$^&$%mna,k/; ##","<EOF>",172))
    def test_comment_case983(self):
        self.assertTrue(TestLexer.checkLexeme("## # a # b ##","<EOF>",173))
    def test_comment_case4(self):
        self.assertTrue(TestLexer.checkLexeme("## #ab\\n \\tc ##","<EOF>",174))
    def test_comment_case5(self):
        self.assertTrue(TestLexer.checkLexeme("####","<EOF>",175))
    def test_comment_case6(self):
        self.assertTrue(TestLexer.checkLexeme("## ## ##","Unterminated Comment",176))
    def test_comment_case7(self):
        self.assertTrue(TestLexer.checkLexeme("##philong ## nhanb ## nhanb ##","nhanb,<EOF>",177))
    def test_comment_case8(self):
        self.assertTrue(TestLexer.checkLexeme("## #### ##","<EOF>",178))
    def test_comment_case9(self):
        self.assertTrue(TestLexer.checkLexeme("## a# a# a# ##","<EOF>",179))
    def test_comment_case10(self):
        self.assertTrue(TestLexer.checkLexeme("## aaa## ##","Unterminated Comment",180))
   

    #ARRAY
    def test_array_case1(self):
        self.assertTrue(TestLexer.checkLexeme("[1,2,3];","[,1,,,2,,,3,],;,<EOF>",181))
    def test_array_case22(self):
        self.assertTrue(TestLexer.checkLexeme("[[1,2],[1,2],[1,2]];","[,[,1,,,2,],,,[,1,,,2,],,,[,1,,,2,],],;,<EOF>",182))
    def test_array_case983(self):
        self.assertTrue(TestLexer.checkLexeme("Let aBC = True","Let,aBC,=,True,<EOF>",183))
    def test_array_case4(self):
        self.assertTrue(TestLexer.checkLexeme("For x In [1,2,3]","For,x,In,[,1,,,2,,,3,],<EOF>",184))
    def test_array_case5(self):                                         
        self.assertTrue(TestLexer.checkLexeme("[[]]","[,[,],],<EOF>",185))
    def test_array_case6(self):
        self.assertTrue(TestLexer.checkLexeme("a < b","a,<,b,<EOF>",186))
    def test_array_case7(self):
        self.assertTrue(TestLexer.checkLexeme("x = 3 + 5","x,=,3,+,5,<EOF>",187))
    def test_array_case8(self):
        self.assertTrue(TestLexer.checkLexeme("While Let philong $philong","While,Let,philong,$philong,<EOF>",188))
    def test_array_case9(self):
        self.assertTrue(TestLexer.checkLexeme("Let a = \"Abc\"","Let,a,=,Abc,<EOF>",189))
    def test_array_case10(self):
        self.assertTrue(TestLexer.checkLexeme("Let a b = 5;","Let,a,b,=,5,;,<EOF>",190))
    # Linh tinh
    def test_compare_case1(self):
        self.assertTrue(TestLexer.checkLexeme("a__","a__,<EOF>",191))
    def test_compare_case2(self):
        self.assertTrue(TestLexer.checkLexeme("; , +",";,,,+,<EOF>",192))
    def test_compare_case983(self):
        self.assertTrue(TestLexer.checkLexeme("Let==","Let,==,<EOF>",193))
    def test_compare_case4(self):
        self.assertTrue(TestLexer.checkLexeme("======","==,==,==,<EOF>",194))
    def test_compare_case5(self):
        self.assertTrue(TestLexer.checkLexeme("===","==,=,<EOF>",195))
    def test_compare_case6(self):
        self.assertTrue(TestLexer.checkLexeme("+++","+,+,+,<EOF>",196))
    def test_compare_case7(self):
        self.assertTrue(TestLexer.checkLexeme("123++","123,+,+,<EOF>",197))
    def test_compare_case8(self):
        self.assertTrue(TestLexer.checkLexeme("123==","123,==,<EOF>",198))
    def test_compare_case9(self):
        self.assertTrue(TestLexer.checkLexeme("TrueFalse","True,False,<EOF>",199))
    def test_compare_case10(self):
        self.assertTrue(TestLexer.checkLexeme("True False True","True,False,True,<EOF>",200))
   

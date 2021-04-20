import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    def test_array_case1(self):
        input = """Function foo(a[5], b) {Constant $taisaotaoquen2conmadeoduoclamgi=
            [1,2,3];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    def test_array_case2(self):
        input = """Function foo(a[5], b) {Let bonnolamcaigimalauvay=
            ["a", "b", "c"];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    def test_array_case3(self):
        input = """Function foo(a[5], b) {Let taohancuocdoi=
            [[1,2],[1,2],[1,2]];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    def test_array_case4(self):
        input = """Function foo(a[5], b) {Let taolaobidaothatsu = 
            [[]];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_array_case5(self):
        input = """Function foo(a[5], b) {Constant $a = 
            [[],[[[]]],[]];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test_array_case6(self):
        input = """Function foo(a[5], b) {Constant $menochu=
            [[[1,2,3],[1,2]],[{
            name: "a",
            b: "c",
            c: "d"
        }]];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test_array_case7(self):
        input = """Function foo(a[5], b) {Let a =
            [[1,2,3];
            }"""
        expect = "Error on line 2 col 20: ;"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test_array_case8(self):
        input = """Function foo(a[5], b) {Constant $something = 
            [[1,2,]];
            }"""
        expect = "Error on line 2 col 18: ]"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    def test_array_case9(self):
        input = """Function foo(a[5], b) {Let a = 
            [1,2,3,];
            }"""
        expect = "Error on line 2 col 19: ]"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    def test_array_case10(self):
        input = """Function foo(a[5], b) {Constant $emthatsungungoc= 
            [,];
            }"""
        expect = "Error on line 2 col 13: ,"
        self.assertTrue(TestParser.checkParser(input,expect,210))
    
    #JSON
    def test_json_case1(self):
        input = """Function foo(a[5], b) {
            Let silly = {
            name: "a",
            b: "c",
            c: "d"
        };
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    def test_json_case2(self):
        input = """Function foo(a[5], b) {
            Constant $a ={
            name: 1,
            b: 2,
            c: "d"
        };
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))
    def test_json_case3(self):
        input = """Function foo(a[5], b) {
            Constant $a ={
            name: [1,2,3],
            b: "STRING",
            c: 123
        };
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))
    def test_json_case4(self):
        input = """Function foo(a[5], b) {
            Let name = {
            name: [[1,2],[2,3]],
            b: True,
            c: "d"
        };
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))
    def test_json_case5(self):
        input = """Function foo(a[5], b) {
            Constant $a ={
            name: {
                a : 123,
                b : [[1,2],[{
                    abcdef : 789,
                    okn : "string"
                }]]
            },
            b: "c",
            c: [1,2,3]
        };
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))
    def test_json_case6(self):
        input = """Function foo(a[5], b) {
            Constant $a ={
            name: "a",
            b: "c",
            c: "d"
        };
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))
    def test_json_case7(self):
        input = """Function foo(a[5], b) {
            Constant $a ={
            name: "a",
            b: "c",
            c: "d",
        };
        }"""
        expect = "Error on line 6 col 8: }"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    def test_json_case8(self):
        input = """Function foo(a[5], b) {
            Constant $a ={
            name: "a",
            b: "c",
            : "d"
        };
        }"""
        expect = "Error on line 5 col 12: :"
        self.assertTrue(TestParser.checkParser(input,expect,218))
    def test_json_case9(self):
        input = """Function foo(a[5], b) {
            Constant $a ={
            name: "a",
            b: "c"
            c: "d"
        };
        }"""
        expect = "Error on line 5 col 12: c"
        self.assertTrue(TestParser.checkParser(input,expect,219))
    def test_json_case10(self):
        input = """Function foo(a[5], b) {
            Constant $a ={
       
        };
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))
    
    #VAR DEC
    def test_variable_case1(self):
        input = """Let a;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    def test_variable_case2(self):
        input = """Let a,b,c,d;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))
    def test_variable_case3(self):
        input = """Let a: String = "abc";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))
    def test_variable_case4(self):
        input = """Let a : String, b = 5, c;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))
    def test_variable_case5(self):
        input = """Let a = "string", b;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))
    def test_variable_case6(self):
        input = """Let a = {
            name: "a",
            b: "c",
            c: "d"
        }, b : JSON = {
            name: [[1,2],[2,3]],
            b: True,
            c: "d"
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))
    def test_variable_case7(self):
        input = """Let a = [[1,2],[2,3]], b = {
            name: [1,2,3],
            b: "STRING",
            c: 123
        }, d : Boolean = True, e = False;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))
    def test_variable_case8(self):
        input = """Let Abc;"""
        expect = "A"
        self.assertTrue(TestParser.checkParser(input,expect,228))
    def test_variable_case9(self):
        input = """Let a b = 5;"""
        expect = "Error on line 1 col 6: b"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    def test_variable_case10(self):
        input = """Let a < 5;"""
        expect = "Error on line 1 col 6: <"
        self.assertTrue(TestParser.checkParser(input,expect,230))
    
    #INSTANT DEC
    def test_instant_case1(self):
        input = """Constant $a123 = 12;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))
    def test_instant_case2(self):
        input = """Constant $a123 : String = 62, $B = "string";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))
    def test_instant_case3(self):
        input = """Constant $a123 : String = 1, $_ = 6, $ABC : Boolean = True;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))
    def test_instant_case4(self):
        input = """Constant $a123 : JSON = {
            name: [[1,2],[2,3]],
            b: True,
            c: "d"
        }, $b = [[],[[[]]],[]];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))
    def test_instant_case5(self):
        input = """Constant $1 : String = [1,2,3];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))
    def test_instant_case6(self):
        input = """Constant abc = 12;"""
        expect = "Error on line 1 col 9: abc"
        self.assertTrue(TestParser.checkParser(input,expect,236))
    def test_instant_case7(self):
        input = """Constant $a;"""
        expect = "Error on line 1 col 11: ;"
        self.assertTrue(TestParser.checkParser(input,expect,237))
    def test_instant_case8(self):
        input = """Constant $a123 : String, $b = 7;"""
        expect = "Error on line 1 col 23: ,"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    def test_instant_case9(self):
        input = """Constant $a, b;"""
        expect = "Error on line 1 col 11: ,"
        self.assertTrue(TestParser.checkParser(input,expect,239))
    def test_instant_case10(self):
        input = """Constant $a123 = 12, b = 7;"""
        expect = "Error on line 1 col 21: b"
        self.assertTrue(TestParser.checkParser(input,expect,240))
    
    #ASSIGN
    def test_assign_case1(self):
        input = """Function foo(a[5], b) {
            a = 7;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))
    def test_assign_case2(self):
        input = """Function foo(a[5], b) {
            aBc = a + (b +c);
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))
    def test_assign_case3(self):
        input = """Function foo(a[5], b) {
            abc = a * 123 + 6 * Call(foo, [1,2]) + [1,2,3];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))
    def test_assign_case4(self):
        input = """Function foo(a[5], b) {
            a[1,2] = aBC[1,2] + ab["name"]["a"];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))
    def test_assign_case5(self):
        input = """Function foo(a[5], b) {
            a["name"] = (a+3) > aBC[1,2] + a[3%b] + ab["name"]["a"];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))
    def test_assign_case6(self):
        input = """Function foo(a[5], b) {
            a[1,2] + b = aBC[1,2] + ab["name"]["a"];
            }"""
        expect = "Error on line 2 col 19: +"
        self.assertTrue(TestParser.checkParser(input,expect,246))
    def test_assign_case7(self):
        input = """Function foo(a[5], b) {
            a["tring"][3] = aBC[1,2] + ab["name"]["a"];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))
    def test_assign_case8(self):
        input = """Function foo(a[5], b) {
            $a = a+b;
            }"""
        expect = "Error on line 2 col 15: ="
        self.assertTrue(TestParser.checkParser(input,expect,248))
    def test_assign_case9(self):
        input = """Function foo(a[5], b) {
            b = $aBC[1,2] ==. ab["name"]["a"];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))
    def test_assign_case10(self):
        input = """Function foo(a[5], b) {
            a["a"]= aBC[1,2] + + a;
            }"""
        expect = "Error on line 2 col 31: +"
        self.assertTrue(TestParser.checkParser(input,expect,250))
    
    #IF
    def test_if_case1(self):
        input = """Function foo(a[5], b) {
            If(a == b) {
            a = 3;
            Return 5;
            }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))
    def test_if_case2(self):
        input = """Function foo(a[5], b) {
            If(a > b + 3 % 7)
        {
            Let a : String = "string", b = 3;  
            a = b[5];
        }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 252))
    def test_if_case3(self):
        input = """Function foo(a[5], b) {
            if(a==2) 
            }"""
        expect = "Error on line 2 col 14: ("
        self.assertTrue(TestParser.checkParser(input, expect, 253))
    def test_if_case4(self):
        input = """Function foo(a[5], b) {
            If(True)
        {
            a = {
                name: 123,
                d: 2
            };
        }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 254))
    def test_if_case5(self):
        input = """Function foo(a[5], b) {
            If(Call(foo,[1,2]))
        {
            a = {
                name: [1,2,3],
                a: 10
            };
        }
        Else
        {
            a = 3;
        }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 255))
    def test_if_case6(self):
        input = """Function foo(a[5], b) {
            If(a + b < 7 && a+b)
        {
            a = 3;
            b = 2;
            Let sum : String = a + b;
        }
        Else
        {
            Return 0;
        }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 256))
    def test_if_case7(self):
        input = """Function foo(a[5], b) {
            If(a == 30)
        {
            Return 3;   
        }
        Elif (a == 4)
        {
            Return 4;
        }
        Elif( a+b+c*d){
            a = 5;
        }
        Else{
            a = d;
        }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 257))
    def test_if_case8(self):
        input = """Function foo(a[5], b) {
            If(a == 3 {
            Return err;
        }
        }"""
        expect = "Error on line 2 col 22: {"
        self.assertTrue(TestParser.checkParser(input, expect, 258))
    def test_if_case9(self):
        input = """Function foo(a[5], b) { If(a == 3)
        {
            Return err;
            }"""
        expect = "Error on line 4 col 13: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 259))
    def test_if_case10(self):
        input = """Function foo(a[5], b) {
            If(a > 2)
            Return nope;
            }"""
        expect = "Error on line 3 col 12: Return"
        self.assertTrue(TestParser.checkParser(input, expect, 260))
    #FOR IN/OF
    def test_for_case1(self):
        input = """Function foo(a[5], b) {
            For i In [1,2,3]{
            a = 5;
        }} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))
    def test_for_case2(self):
        input = """Function foo(a[5], b) {
            For i In [[1,2],[1,2],3]{
            a = 5;
            Call(foo, [1,2,3]);
        }
        } """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))
    def test_for_case3(self):
        input = """Function foo(a[5], b) {
            For i Of {
            name: "abc",
            a : 123
        }{
            a = 3;
        }
        } """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))
    def test_for_case4(self):
        input = """Function foo(a[5], b) {
            For i In [{
            name: "abc",
            a : 123
        },{
            name: "abc",
            a : 123
        }]{
            a = {
            name: "abc",
            a : 123
        };
        } 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))
    def test_for_case5(self):
        input = """Function foo(a[5], b) {
            For a + b In [[1,2],[1,2],3]{
            a = 5;
            Call(foo, [1,2,3]);
        }
        } """
        expect = "Error on line 2 col 18: +"
        self.assertTrue(TestParser.checkParser(input,expect,265))
    def test_for_case6(self):
        input = """Function foo(a[5], b) {
            For $i In [[1,2],[1,2],3]{
            If(a == 30)
            {
                Return 3;   
            }
            Elif (a == 4)
            {
                Return 4;
            }
            Elif( a+b+c*d){
                a = 5;
            }
            Else{
                a = d;
            }
        }
        } """
        expect = "Error on line 2 col 16: $i"
        self.assertTrue(TestParser.checkParser(input,expect,266))
    def test_for_case7(self):
        input = """Function foo(a[5], b) {
            For a  In {
            name: "abc",
            a : 123
        }{
            a = 5;
            Call(foo, [1,2,3]);
        } 
        }"""
        expect = "Error on line 2 col 22: {"
        self.assertTrue(TestParser.checkParser(input,expect,267))
    def test_for_case8(self):
        input = """Function foo(a[5], b) {
            For a Of {
            name: "abc",
            a : 123
        }{
            For a Of {
            name: "abc",
            a : 123
            }{
                a = 5;
            }
        } 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))
    def test_for_case9(self):
        input = """Function foo(a[5], b) {
            For a Of {
            name: "abc",
            a : 123,
        }{
            a   =  5;
        } 
        }"""
        expect = "Error on line 5 col 8: }"
        self.assertTrue(TestParser.checkParser(input,expect,269))
    def test_for_case10(self):
        input = """Function foo(a[5], b) {
            For a Of { "string"
        }{
            a   =  5;
        } 
        }"""
        expect = "Error on line 2 col 23: string"
        self.assertTrue(TestParser.checkParser(input,expect,270))
    
    #WHILE
    def test_while_case1(self):
        input = """
        Function foo(a[5], b) {
            While(a = b){
                a = b;
            }
            }"""
        expect = "Error on line 3 col 20: ="
        self.assertTrue(TestParser.checkParser(input,expect,271))
    def test_while_case2(self):
        input = """Function foo(a[5], b) {
            While(a + b){
                Break;
                Continue;
                a = b;
            }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))
    def test_while_case3(self):
        input = """
        Function foo(a[5], b) {
            While(a == b){
                a = b;
                Return a*5;
            }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))
    def test_while_case4(self):
        input = """Function foo(a[5], b) {
            While(a == b && 5){
                a = 3;
            }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))
    def test_while_case5(self):
        input = """Function foo(a[5], b) {
            While(a == b || a&&b){
                a = b + 3;
            }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))
    def test_while_case6(self):
        input = """Function foo(a[5], b) {
            While(a == 5;){
                a = b;
            }
            }"""
        expect = "Error on line 2 col 24: ;"
        self.assertTrue(TestParser.checkParser(input,expect,276))
    def test_while_case7(self):
        input = """Function foo(a[5], b) {
            While(a == 5){
                a = b;
                ##
                # 
                ##
            }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))
    def test_while_case8(self):
        input = """Function foo(a[5], b) {
            While(If(a == b){a = 5;}){
                a = b;
                ##
                #   Vi sao anh chan em the nay ??????
                #
                ##
            }
            }"""
        expect = "Error on line 2 col 18: If"
        self.assertTrue(TestParser.checkParser(input,expect,278))
    def test_while_case9(self):
        input = """Function foo(a[5], b) {
            While(-10){
                a = b;
                Let question="Why?????";
            }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))
    def test_while_case10(self):
        input = """Function foo(a[5], b) {
            While(a == -5){
                a = b;
            }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,280))
    
    #CALL
    def test_call_case1(self):
        input = """Function foo(a[5], b) {
            Call(foo, [2 + x, 4 / y]);
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))
    def test_call_case2(self):
        input = """Function foo(a[5], b) {
            Let status = "phanno";
            Call(uuu, []);
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))
    def test_call_case3(self):
        input = """Function foo(a[5], b) {
            Let chanthatsuay = "a";
            Constant $alo = Call(foo, [[1,2,3],[1,2]]);
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))
    def test_call_case4(self):
        input = """Function foo(a[5], b) {
            Constant $leuleune = Call(foo, [x, 1+2+3]);
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))
    def test_call_case5(self):
        input = """Function foo(a[5], b) {
            Let a = Call(foo, [{
            name: "string",
            a : 1
        }, 4 / y]);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))
    def test_call_case6(self):
        input = """Function foo(a[5], b) {
            Let something = Call(foo, [{
            name: 1,
            a : 2
        }]);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,286))
    def test_call_case7(self):
        input = """Function foo(a[5], b) {Let b = 
            Call(foo fo, [2 + x, 4 / y]);
            }"""
        expect = "Error on line 2 col 21: fo"
        self.assertTrue(TestParser.checkParser(input,expect,287))
    def test_call_case8(self):
        input = """Function foo(a[5], b) {Constant $a =
            Call(foo, [x = 3]);
            }"""
        expect = "Error on line 2 col 25: ="
        self.assertTrue(TestParser.checkParser(input,expect,288))
    def test_call_case9(self):
        input = """Function foo(a[5], b) {
            Let qualangungoc = Call(foo, [1,2,]);
            }"""
        expect = "Error on line 2 col 46: ]"
        self.assertTrue(TestParser.checkParser(input,expect,289))
    def test_call_case10(self):
        input = """Function foo(a[5], b) {
            Let thatlangungoc = Call(foo, [Call(foooo, [1,2]), 4 / y]);
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,290))
    
    #FUNC
    def test_function_case1(self):
        input = """
        Constant $a = 10;
        Function foo(a[5], b) {
            Constant $b: String = "Story of Yanxi Place";
            Let i = 0;
            While (i < 5) {
                a[i] = (b + 1) * $a;
                Let u: String = i + 1;
                If (a[u] == 10) {
                    Return $b;
                }
                question = 30 + phut ;
            }
            Return $b + ": bon m chua xong that a ";
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))
    def test_function_case2(self):
        input = """
        Constant $a = 10;
        Function foo(a[5,a], a,b) {
            Constant $b: String = "Story of Yanxi Place";
            Let i = 0;
            While (i < 5) {
                a[i] = (b + 1) * $a;
                Let u: String = i + 1;
                If (a[u] == 10) {
                    Return $b;
                }
                question = 30 + phut ;
            }
            Return $b + ": bon m chua xong that a ";
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,292))
    def test_function_case3(self):
        input = """
        Constant $a = 10;
        Function foo(a[]) {
            Constant $b: String = "Story of Yanxi Place";
            Let i = 0;
            While (i < 5) {
                a[i] = (b + 1) * $a;
                Let u: String = i + 1;
                If (a[u] == 10) {
                    Return $b;
                }
                question = 30 + phut ;
            }
            Return $b + ": bon m chua xong that a ";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,293))
    def test_function_case4(self):
        input = """
        Constant $a = 10;
        Function foo(a[1,2,3,4]) {
            Constant $b: String = "Story of Yanxi Place";
            Let i = 0;
            While (i < 5) {
                a[i] = (b + 1) * $a;
                Let u: String = i + 1;
                If (a[u] == 10) {
                    Return $b;
                }
                question = 30 + phut ;
            }
            Return $b + ": bon m chua xong that a ";
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,294))
    def test_function_case5(self):
        input = """
        Constant $a = 10;
        Function foo(a[5], {
            a: "string",
            b : 3
        }) {
            Constant $b: String = "Story of Yanxi Place";
            Let i = 0;
            While (i < 5) {
                a[i] = (b + 1) * $a;
                Let u: String = i + 1;
                If (a[u] == 10) {
                    Return $b;
                }
                question = 30 + phut ;
            }
            Return $b + ": bon m chua xong that a ";
        }
        """
        expect = "Error on line 3 col 27: {"
        self.assertTrue(TestParser.checkParser(input,expect,295))
    def test_function_case6(self):
        input = """
        Constant $a = 10;
        Function foo(a) {
            Constant $b: String = "Story of Yanxi Place";
            Let i = 0;
            While (i < 5) {
                a[i] = (b + 1) * $a;
                Let u: String = i + 1;
                If (a[u] == 10) {
                    Return $b;
                }
                question = 30 + phut ;
            }
            Return $b + ": bon m chua xong that a ";
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))
    def test_function_case7(self):
        input = """
        Constant $a = 10;
        Function foo(Call(foo, [1,2,3])) {
            Constant $b: String = "Story of Yanxi Place";
            Let i = 0;
            While (i < 5) {
                a[i] = (b + 1) * $a;
                Let u: String = i + 1;
                If (a[u] == 10) {
                    Return $b;
                }
                question = 30 + phut ;
            }
            Return $b + ": bon m chua xong that a ";
        }
        """
        expect = "Error on line 3 col 39: )"
        self.assertTrue(TestParser.checkParser(input,expect,297))
    def test_function_case8(self):
        input = """
        Constant $a = 10;
        Function foo(a = b) {
            Constant $b: String = "Story of Yanxi Place";
            Let i = 0;
            While (i < 5) {
                a[i] = (b + 1) * $a;
                Let u: String = i + 1;
                If (a[u] == 10) {
                    Return $b;
                }
                question = 30 + phut ;
            }
            Return $b + ": bon m chua xong that a ";
        }
        """
        expect = "Error on line 3 col 23: ="
        self.assertTrue(TestParser.checkParser(input,expect,298))
    def test_function_case9(self):
        input = """
        Constant $a = 10;
        Function foo($a) {
            Constant $b: String = "Story of Yanxi Place";
            Let i = 0;
            While (i < 5) {
                a[i] = (b + 1) * $a;
                Let u: String = i + 1;
                If (a[u] == 10) {
                    Return $b;
                }
                question = 30 + phut ;
            }
            Return $b + ": bon m chua xong that a ";
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))
    def test_function_case10(self):
        input = """
        Constant $a = 10;
        Function foo() {
            Constant $b: String = "Story of Yanxi Place";
            Let i = 0;
            While (i < 5) {
                a[i] = (b + 1) * $a;
                Let u: String = i + 1;
                If (a[u] == 10) {
                    Return $b;
                }
                question = 30 + phut ;
            }
            Return $b + ": bon m chua xong that a ";
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,300))
    
##  #  ##
    def test_function_case10(self):
        input = """
        Function foo(m, n){
                        Let x = Call(foo1, ["Let","me"]) +  Call(foo1, ["Let","me"]) - a[3,2];
                        Return Call(foo, []);
                    }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,1004))

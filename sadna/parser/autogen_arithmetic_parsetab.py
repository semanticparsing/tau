
# autogen_arithmetic_parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = ',\xa1\x9c\xf9\xd0K\xfb\xe9\xf8\xe7\xa1AF\x98u\x00'
    
_lr_action_items = {'RPAREN':([4,5,6,8,9,10,15,16,17,20,21,24,33,37,38,41,42,43,44,45,],[-13,-12,7,-14,-13,-8,-10,-11,-9,-28,-25,-27,45,-26,-29,-22,-20,-21,-23,-24,]),'NAME':([0,1,3,4,9,10,12,13,15,17,18,23,25,27,28,30,31,32,34,35,36,47,],[2,2,2,5,5,-8,-3,20,-10,-9,-5,-4,20,38,20,20,20,20,-2,20,-6,-7,]),'RCURLY':([12,13,18,20,21,22,23,24,26,35,37,38,39,41,42,43,44,45,46,],[-3,-17,-5,-28,-25,-18,-4,-27,36,-16,-26,-29,-19,-22,-20,-21,-23,-24,-15,]),'NEWLINE':([4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,22,23,24,26,35,36,37,38,39,41,42,43,44,45,46,],[-13,-12,8,11,-14,-13,17,11,-3,-17,14,-10,8,-9,-5,-28,-25,-18,-4,-27,35,-16,47,-26,-29,-19,-22,-20,-21,-23,-24,-15,]),'NUMBER':([12,13,18,23,25,27,28,29,30,31,32,35,40,],[-3,21,-5,-4,21,37,21,21,21,21,21,21,37,]),'TIMES':([19,20,21,24,33,37,38,39,41,42,43,44,45,],[29,-28,-25,32,29,-26,-29,29,-22,29,29,-23,-24,]),'LCURLY':([7,11,],[12,12,]),'EQUALS':([19,20,21,24,37,38,41,42,43,44,45,],[28,-28,-25,-27,-26,-29,-22,-20,-21,-23,-24,]),'COMMA':([4,5,6,8,9,10,14,15,16,17,],[-13,-12,10,-14,-13,-8,10,-10,10,-9,]),'LPAREN':([2,12,13,18,23,25,28,30,31,32,35,],[4,-3,25,-5,-4,25,25,25,25,25,25,]),'PLUS':([19,20,21,24,33,37,38,39,41,42,43,44,45,],[30,-28,-25,-27,30,-26,-29,30,-22,-20,-21,-23,-24,]),'MINUS':([12,13,18,19,20,21,23,24,25,28,29,30,31,32,33,35,37,38,39,41,42,43,44,45,],[-3,27,-5,31,-28,-25,-4,-27,27,27,40,27,27,27,31,27,-26,-29,31,-22,-20,-21,-23,-24,]),'$end':([1,3,34,36,47,],[0,-1,-2,-6,-7,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'functions':([0,1,3,],[1,3,3,]),'rcurly':([26,],[34,]),'equation':([13,35,],[22,46,]),'term':([13,25,28,30,31,32,35,],[19,33,39,42,43,44,19,]),'lcurly':([7,11,],[13,18,]),'literal':([13,25,28,29,30,31,32,35,],[24,24,24,41,24,24,24,24,]),'comma':([6,8,14,16,],[9,15,15,9,]),'paramlist':([4,9,],[6,16,]),'equations':([13,],[26,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> functions","S'",1,None,None,None),
  ('functions -> functions functions','functions',2,'p_functions','/Users/corwin/var/workspace/Teaching.DSL.RipOff.Python/src/parser/arithmetic_parser.py',63),
  ('functions -> NAME LPAREN paramlist RPAREN lcurly equations rcurly','functions',7,'p_function','/Users/corwin/var/workspace/Teaching.DSL.RipOff.Python/src/parser/arithmetic_parser.py',67),
  ('lcurly -> LCURLY','lcurly',1,'p_no_newline','/Users/corwin/var/workspace/Teaching.DSL.RipOff.Python/src/parser/arithmetic_parser.py',75),
  ('lcurly -> lcurly NEWLINE','lcurly',2,'p_no_newline','/Users/corwin/var/workspace/Teaching.DSL.RipOff.Python/src/parser/arithmetic_parser.py',76),
  ('lcurly -> NEWLINE lcurly','lcurly',2,'p_no_newline','/Users/corwin/var/workspace/Teaching.DSL.RipOff.Python/src/parser/arithmetic_parser.py',77),
  ('rcurly -> RCURLY','rcurly',1,'p_no_newline','/Users/corwin/var/workspace/Teaching.DSL.RipOff.Python/src/parser/arithmetic_parser.py',78),
  ('rcurly -> RCURLY NEWLINE','rcurly',2,'p_no_newline','/Users/corwin/var/workspace/Teaching.DSL.RipOff.Python/src/parser/arithmetic_parser.py',79),
  ('comma -> COMMA','comma',1,'p_no_newline','/Users/corwin/var/workspace/Teaching.DSL.RipOff.Python/src/parser/arithmetic_parser.py',80),
  ('comma -> COMMA NEWLINE','comma',2,'p_no_newline','/Users/corwin/var/workspace/Teaching.DSL.RipOff.Python/src/parser/arithmetic_parser.py',81),
  ('comma -> NEWLINE comma','comma',2,'p_no_newline','/Users/corwin/var/workspace/Teaching.DSL.RipOff.Python/src/parser/arithmetic_parser.py',82),
  ('paramlist -> paramlist comma paramlist','paramlist',3,'p_paramlist_comma','/Users/corwin/var/workspace/Teaching.DSL.RipOff.Python/src/parser/arithmetic_parser.py',86),
  ('paramlist -> NAME','paramlist',1,'p_paramlist_from_name','/Users/corwin/var/workspace/Teaching.DSL.RipOff.Python/src/parser/arithmetic_parser.py',90),
  ('paramlist -> <empty>','paramlist',0,'p_paramlist_empty','/Users/corwin/var/workspace/Teaching.DSL.RipOff.Python/src/parser/arithmetic_parser.py',94),
  ('paramlist -> paramlist NEWLINE','paramlist',2,'p_paramlist_newline','/Users/corwin/var/workspace/Teaching.DSL.RipOff.Python/src/parser/arithmetic_parser.py',98),
  ('equations -> equations NEWLINE equation','equations',3,'p_equations_newline_equations','/Users/corwin/var/workspace/Teaching.DSL.RipOff.Python/src/parser/arithmetic_parser.py',102),
  ('equations -> equations NEWLINE','equations',2,'p_equations_newline','/Users/corwin/var/workspace/Teaching.DSL.RipOff.Python/src/parser/arithmetic_parser.py',106),
  ('equations -> <empty>','equations',0,'p_equations_empty','/Users/corwin/var/workspace/Teaching.DSL.RipOff.Python/src/parser/arithmetic_parser.py',110),
  ('equations -> equation','equations',1,'p_equations_one','/Users/corwin/var/workspace/Teaching.DSL.RipOff.Python/src/parser/arithmetic_parser.py',114),
  ('equation -> term EQUALS term','equation',3,'p_equation','/Users/corwin/var/workspace/Teaching.DSL.RipOff.Python/src/parser/arithmetic_parser.py',118),
  ('term -> term PLUS term','term',3,'p_term_plusminus_term','/Users/corwin/var/workspace/Teaching.DSL.RipOff.Python/src/parser/arithmetic_parser.py',129),
  ('term -> term MINUS term','term',3,'p_term_plusminus_term','/Users/corwin/var/workspace/Teaching.DSL.RipOff.Python/src/parser/arithmetic_parser.py',130),
  ('term -> term TIMES literal','term',3,'p_term_times_literal','/Users/corwin/var/workspace/Teaching.DSL.RipOff.Python/src/parser/arithmetic_parser.py',142),
  ('term -> literal TIMES term','term',3,'p_literal_times_term','/Users/corwin/var/workspace/Teaching.DSL.RipOff.Python/src/parser/arithmetic_parser.py',149),
  ('term -> LPAREN term RPAREN','term',3,'p_term_parenthesis','/Users/corwin/var/workspace/Teaching.DSL.RipOff.Python/src/parser/arithmetic_parser.py',156),
  ('literal -> NUMBER','literal',1,'p_literal_number','/Users/corwin/var/workspace/Teaching.DSL.RipOff.Python/src/parser/arithmetic_parser.py',160),
  ('literal -> MINUS NUMBER','literal',2,'p_literal_minus_numer','/Users/corwin/var/workspace/Teaching.DSL.RipOff.Python/src/parser/arithmetic_parser.py',164),
  ('term -> literal','term',1,'p_term_literal','/Users/corwin/var/workspace/Teaching.DSL.RipOff.Python/src/parser/arithmetic_parser.py',168),
  ('term -> NAME','term',1,'p_term_name','/Users/corwin/var/workspace/Teaching.DSL.RipOff.Python/src/parser/arithmetic_parser.py',172),
  ('term -> MINUS NAME','term',2,'p_term_minus_name','/Users/corwin/var/workspace/Teaching.DSL.RipOff.Python/src/parser/arithmetic_parser.py',176),
]

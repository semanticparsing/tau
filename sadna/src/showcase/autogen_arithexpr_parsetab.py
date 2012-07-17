
# autogen_arithexpr_parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = ',\xa1\x9c\xf9\xd0K\xfb\xe9\xf8\xe7\xa1AF\x98u\x00'
    
_lr_action_items = {'RPAREN':([2,3,4,11,12,13,14,15,17,18,19,],[-28,-25,-27,19,-26,-29,-20,-21,-22,-23,-24,]),'NAME':([0,5,6,7,8,10,],[2,2,13,2,2,2,]),'NUMBER':([0,5,6,7,8,9,10,16,],[3,3,12,3,3,3,3,12,]),'TIMES':([1,2,3,4,11,12,13,14,15,17,18,19,],[9,-28,-25,10,9,-26,-29,9,9,-22,-23,-24,]),'PLUS':([1,2,3,4,11,12,13,14,15,17,18,19,],[7,-28,-25,-27,7,-26,-29,-20,-21,-22,-23,-24,]),'LPAREN':([0,5,7,8,10,],[5,5,5,5,5,]),'MINUS':([0,1,2,3,4,5,7,8,9,10,11,12,13,14,15,17,18,19,],[6,8,-28,-25,-27,6,6,6,16,6,8,-26,-29,-20,-21,-22,-23,-24,]),'$end':([1,2,3,4,12,13,14,15,17,18,19,],[0,-28,-25,-27,-26,-29,-20,-21,-22,-23,-24,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'term':([0,5,7,8,10,],[1,11,14,15,18,]),'literal':([0,5,7,8,9,10,],[4,4,4,4,17,4,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> term","S'",1,None,None,None),
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

/**
 * @name Using is_superuser inside assert statement
 * @description Call to is_superuser inside assert statement 
   will be ignored when running in optimized mode
 * @kind problem
 * @tags security
 * @problem.severity error 
 * @id py/superuser-in-assert
 */

import python

from AstNode ast, Assert assert
where
  assert.contains(ast) and
  ast.(Call).getFunc().(Name).getId() = "is_superuser"
select ast, "`is_superuser` used within the assert statement"

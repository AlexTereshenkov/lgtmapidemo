/**
 * @name Using a deprecated pyCrypto package
 * @description Using an unmaintained tool kit with multiple security 
   issues makes your code vulnerable to attack.
 * @kind problem
 * @tags security
 * @problem.severity error
 * @id py/using-insecure-pycrypto-package
 */

import python

from ImportExpr imp, Stmt s, Expr e, string moduleName
where
  moduleName = imp.getName() and
  s.getASubExpression() = e and
  (e = imp or e.contains(imp)) and
  (moduleName.matches("Crypto") or moduleName.matches("Crypto.%"))
select imp, "pyCrypto package has multiple security issues"
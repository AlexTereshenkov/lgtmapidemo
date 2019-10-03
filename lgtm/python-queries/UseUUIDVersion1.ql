/**
 * @name Using a uuid1 for generating UUID
 * @description uuid1 will use machine's network address 
   for generating UUID and may compromise privacy.
 * @kind problem
 * @tags security
 * @problem.severity error
 * @id py/using-uuid1-for-UUID
 */

import python

from CallNode call
where
  call = Value::named("uuid.uuid1").getACall()
  or
  call = Value::named("uuid.UUID").getACall() and
  (
    call.getArgByName("version").getNode().(IntegerLiteral).getValue() = 1 or
    call.getArg(5).getNode().(IntegerLiteral).getValue() = 1
  )
select call, "uuid1 will use machine's network address and may compromise privacy."
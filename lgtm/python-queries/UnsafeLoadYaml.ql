/**
 * @name Using insecure yaml.load function
 * @description yaml.load function may be unsafe 
   when loading data from untrusted sources
 * @kind problem
 * @tags security
 * @problem.severity error
 * @id py/using-yaml-load
 */

import python

from CallNode call
where call = Value::named("yaml.load").getACall()
select call.getNode(), "yaml.load function may be unsafe when loading data from untrusted sources. Use yaml.safe_load instead."

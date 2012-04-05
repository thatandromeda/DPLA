import cherrypy
from dpla_timeline import timeline

class HelloWorld(object):
    def index(self):
        return """
        <html>
        	<head>
        	</head>
        	<body>
        		<form action="getParam" method="post">
        			Query: <input type='text' name='param' /><br /><br />
        			# of results: <input type='int' name='limit' size=2 /><br />
	        		<input type='submit' value='Timeline it!' />
	        	</form>
        	</body>
        </html>
        """    
    index.exposed = True

    def getParam(self, param, limit):
    	timeline(param, limit)
    	return param
    
    getParam.exposed = True
    	
cherrypy.quickstart(HelloWorld())
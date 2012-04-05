import cherrypy
from dpla_timeline import timeline

class HelloWorld(object):
    def index(self):
        return """
        <html>
        	<head>
        	</head>
        	<body>
        		hello world<br /><br />yup
        		<form action="getParam" method="post">
        			<input type='text' name='param' />
	        		<input type='submit' value='Timeline it!' />
	        	</form>
        	</body>
        </html>
        """    
    index.exposed = True

    def getParam(self, param):
    	timeline(param)
    	return True
    
    getParam.exposed = True
    	
cherrypy.quickstart(HelloWorld())
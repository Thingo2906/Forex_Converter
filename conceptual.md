##### Conceptual Exercise

# Answer the following questions below:

* What are important differences between Python and JavaScript?*
__We use JavaScript for client-side, and use Python for the service-side.__

**Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you can try to get a missing key (like "c") without your programming crashing.**

_Method1: We use get(x, default) function to return the default value for the key "c"._
    print({"a": 1, "b": 2}.get("c", 3)) //3"

_Method2_: Adding the value for c, so the dictionary will get new key_value and add it at the end of itself.
     {"a": 1, "b" : 2}["c"]= 3;
  
**What is a unit test?**
 _Unit Testing is the process of checking small pieces of code_

**What is an integration test?**
_Integration test is testing multiple unit, and how they intergrate._

**What is the role of web application framework, like Flask?**
_Flask is a tool that is used in Python to help developer to create web server._ 

**You can pass information to Flask either as a parameter in a route URL (like '/foods/pretzel') or using a URL query param (like 'foods?type=pretzel'). How might you choose which one is a better fit for an application?**
_If the application has to use POST request with form submission, we should use a URL query param to see which value is set in._

**How do you collect data from a URL placeholder parameter using Flask?**
_You collect data from a URL placeholder param in Flask by storing it as a variable under the same variable name in the app route._

**How do you collect data from the query string using Flask?**
_We collect data from the query string in Flask using 'flask.request.args.get()'._

**How do you collect data from the body of the request using Flask?**
_Use request.form to get the key/value pairs in the body, from a HTML post form, or JavaScript request that isn't JSON encoded_

**What is a cookie and what kinds of things are they commonly used for?**
_Cookies collect user data stored on the user's computer web browser._


**What is the session object in Flask?**
 _Flask session are a "magic dictinary". Session contain information for the current browser._ 

**What does Flask's `jsonify()` do?**
 _jsonify() is a helper method provided by Flask to properly return JSON data_

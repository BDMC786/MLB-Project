# Make a simple app to test if an href attribute can be used to link to routes based on drop down selection

# This folder allows me to take user input from a text box and modify the template based on the input. 
# Next is to try this with a drop box. Then I can go about writing scrape functions for a team.
# Does a drop box allow capturing the value and text, or just the text??
#Source, includes dicumentation relevant to flask and input: https://stackoverflow.com/questions/12277933/send-data-from-a-textbox-into-flask
# http://flask.pocoo.org/docs/quickstart/#accessing-request-data
# http://wtforms.simplecodes.com/docs/1.0.2/crash_course.html
# http://flask.pocoo.org/docs/patterns/wtforms/

#TEST: import the scrape file and call the function

from flask import Flask, request, render_template
import scrape

app = Flask(__name__)

team_dict = {
"A's" : ["https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Oakland_A%27s_logo.svg/1200px-Oakland_A%27s_logo.svg.png","athletics"], 
"Angels" : ["https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Los_Angeles_Angels_of_Anaheim.svg/1200px-Los_Angeles_Angels_of_Anaheim.svg.png", "angels"], 
"Astros" : ["https://images.homedepot-static.com/productImages/1dc1f2e5-fa15-427e-9b22-13d8c6fca205/svn/orange-fanmats-sports-rugs-18136-64_1000.jpg", "astros"], #does not link
"Blue Jays" : ["https://upload.wikimedia.org/wikipedia/en/thumb/b/ba/Toronto_Blue_Jays_logo.svg/1200px-Toronto_Blue_Jays_logo.svg.png", "bluejays"], #does not link
"Braves" : ["https://a2.espncdn.com/combiner/i?img=%2Fi%2Fteamlogos%2Fmlb%2F500%2Fatl.png", "braves"], 
"Brewers" : ["https://upload.wikimedia.org/wikipedia/en/thumb/1/11/Milwaukee_Brewers_Logo.svg/1200px-Milwaukee_Brewers_Logo.svg.png", "brewers"], 
"Cardinals" : ["https://upload.wikimedia.org/wikipedia/en/thumb/9/9d/St._Louis_Cardinals_logo.svg/1200px-St._Louis_Cardinals_logo.svg.png", "cardinals"], 
"Cubs" : ["https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Chicago_Cubs_logo.svg/1200px-Chicago_Cubs_logo.svg.png", "cubs"], 
"Dbacks" : ["https://www.mlbstatic.com/mlb.com/images/share/109.jpg", "dbacks"], 
"Dodgers" : ["https://cdn.bleacherreport.net/images/team_logos/328x328/los_angeles_dodgers.png", "dodgers"], 
"Giants" : ["https://images-na.ssl-images-amazon.com/images/I/81t%2BIQz-T4L.SY679.jpg", "giants"], 
"Indians": ["https://tse2.mm.bing.net/th?id=OIP.KBdIk7Mrn6en2kmN4cFCdQHaFs&pid=Api&P=0&w=229&h=177", "indians"], 
"Mariners" : ["https://images-na.ssl-images-amazon.com/images/I/91IqBdEZPSL.SY741.jpg", "mariners"], 
"Marlins" : ["https://www.mlbstatic.com/mlb.com/images/share/146.jpg", "marlins"], 
"Mets" : ["https://images-na.ssl-images-amazon.com/images/I/816CbeDIoIL.SY606.jpg", "mets"], 
"Nationals" : ["https://upload.wikimedia.org/wikipedia/en/thumb/a/a3/Washington_Nationals_logo.svg/1200px-Washington_Nationals_logo.svg.png", "nationals"], 
"Orioles" : ["http://cdn0.sbnation.com/assets/4081059/o_s.png", "orioles" ], 
"Padres" : ["https://rfathead-res.cloudinary.com/image/upload/q_auto/c_pad,h_3000/g_north,c_crop,h_3000,w_3000/c_pad,h_3000,w_3000/prodplus/63-63815_mlb_san_diego_padres_2018_realbig_logo_rm34_pdp.jpg", "padres"], 
"Phillies" : ["https://images-na.ssl-images-amazon.com/images/I/617ma53aQWL.SX425.jpg", "phillies"], 
"Pirates" : ["https://1000logos.net/wp-content/uploads/2018/05/Pittsburgh-Pirates-Logo.png", "pirates"], 
"Rangers" : ["https://www.pnglot.com/pngfile/detail/23-236596_texas-rangers-logo-texas-rangers-t-svg.png", "rangers"], 
"Rays" : ["http://www.phillyphanatics.com/wp-content/uploads/2010/12/Tampa-Bay-Rays.jpg", "rays"], #shows rangers?
"Reds" : ["https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Cincinnati_Reds_Logo.svg/1200px-Cincinnati_Reds_Logo.svg.png", "reds"], 
"Red Sox" : ["https://diginomica.com/sites/default/files/images/2019-07/redsox.jpg", "redsox"], 
"Rockies" : ["https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Colorado_Rockies_logo.svg/1200px-Colorado_Rockies_logo.svg.png", "rockies"], 
"Royals" : ["https://www.clipartwiki.com/clipimg/detail/49-497369_the-kansas-city-royals-vs-kc-royals-logo.png", "royals"], 
"Tigers" : ["https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Detroit_Tigers_logo.svg/1200px-Detroit_Tigers_logo.svg.png", "tigers"], 
"Twins" : ["http://content.sportslogos.net/logos/53/65/full/1196.png", "twins"], 
"White Sox" : ["https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Chicago_White_Sox.svg/1200px-Chicago_White_Sox.svg.png", "whitesox"], 
"Yankees" : ["http://images.fanpop.com/images/image_uploads/---new-york-yankees-223768_1500_1500.jpg", "yankees"]
}

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    team = request.form['text']
    background = team_dict[team][0]
#     print(background)
    record = "100-55"
    return render_template("results.html",  background =  background, record = record )

if __name__=='__main__':
    app.run(debug=True)
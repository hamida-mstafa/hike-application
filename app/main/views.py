from flask_login import login_required


@main.route(', methods = ['GET','POST'])
@login_required
def new_review(id):

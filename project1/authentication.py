"""
functions for user authentication

@version: 1.0
@since: 2018-10-01
@author: Christoph Theis
"""

def login(username, password):
    """
    function to check credentials vs text file

    @param username: login username
    @type username: str
    @param password: password
    @type password: str
    @return: login success as boolean
    @rtype: bool
    """
    try:
        user_file = open('D:/Benutzer/users.txt')
        user_buf = user_file.read()
        users = [line.split('|') for line in user_buf.split('\n')]
        return [username, password] in users
    except IOError:
        print "I can't authenticate you."
        return False

def logout():
    print 'You are now logged out.'

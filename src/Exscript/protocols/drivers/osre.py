# Copyright (C) 2007-2010 Samuel Abels.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2, as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
"""
A driver for AlaxalA OS-RE(include Hitachi ROUTE-OS).
"""
import re
from Exscript.protocols.drivers.driver import Driver
from Exscript.protocols.drivers.ios    import _prompt_re

_user_re     = [re.compile(r'[\r\n]User: $')]
_password_re = [re.compile(r'[\r\n](Telnet password:|Password:) $')]
_osre_re    = re.compile(r'\bHitachi\b', re.I)

class OSREDriver(Driver):
    def __init__(self):
        Driver.__init__(self, 'osre')
        self.user_re     = _user_re
        self.password_re = _password_re
        self.prompt_re   = _prompt_re

    def check_head_for_os(self, string):
        if _osre_re.search(string):
            return 75
        return 0

    def auto_authorize(self, conn, account, flush, bailout):
        conn.send('enable\r')
        conn.app_authorize(account, flush, bailout)

# The MIT License (MIT)
#
# Copyright (c) 2016 Francis T. O'Donovan
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""Test main nameshark_vcard methods."""

# coding=utf-8

import pytest
import vobject

import nameshark_vcard.nameshark_vcard as nv

FIRST_NAME = 'John'
SURNAME = 'Smith'
FN_FIELD = FIRST_NAME + ' ' + SURNAME
NAMES = nv.NAMES(FIRST_NAME, SURNAME)

VCARD = 'BEGIN:VCARD\nFN:' + FN_FIELD + '\nEND:VCARD'

COMPONENT = next(vobject.readComponents(VCARD))

ENTRY = {'details': '', 'first': FIRST_NAME, 'last': SURNAME, 'photoData': ''}

CONTACTS = [ENTRY]

JSON_STR = \
    '{\n"contacts":[\n{\n"details":"",\n' + '"first":"' + FIRST_NAME + \
    '",\n"last":"' + SURNAME + '",\n"photoData":""\n}\n],\n' + '"name":"group"\n}'

GROUP_NAME = 'group'


@pytest.mark.incremental
def test_get_pp_names():
    """Test get_pp_names() function."""
    assert nv.get_pp_names(FN_FIELD) == NAMES


@pytest.mark.incremental
def test_get_names():
    """Test get_names() function."""
    assert nv.get_names(FN_FIELD) == NAMES


@pytest.mark.incremental
def test_extract_contact_from_component():
    """Test extract_contact_from_component() function."""
    assert nv.extract_contact_from_component(COMPONENT) == ENTRY


@pytest.mark.incremental
def test_extract_contacts_from_vcard():
    """Test extract_contacts_from_vcard() function."""
    assert nv.extract_contacts_from_vcard(VCARD) == CONTACTS


@pytest.mark.incremental
def test_convert_to_nameshark():
    """Test convert_to_nameshark() function."""
    assert nv.convert_to_nameshark(GROUP_NAME, CONTACTS).replace(' ', '') == JSON_STR


@pytest.mark.incremental
def test_vcard_to_nameshark():
    """Test vcard_to_nameshark() function."""
    assert nv.vcard_to_nameshark(VCARD, GROUP_NAME).replace(' ', '') == JSON_STR

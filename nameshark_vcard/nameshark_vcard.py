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
"""Convert vCard-formatted string to the JSON format expected by Name Shark."""

# coding=utf-8

import base64
import json
import collections

import argparse
import vobject

NAMES = collections.namedtuple('Names', ['first_name', 'surname'])


def get_pp_names(fn_field):
    """
    Use probablepeople to extract firstname/surname from vCard 'fn' field.

    :param fn_field: the input vCard 'fn' field.
    :return: a namedtuple containing the first name and surname.

    >>> get_names('John Smith')
    Extracting data for John Smith
    Names(first_name='John', surname='Smith')
    """
    first_name = None
    surname = None

    try:
        import probablepeople as pp  # not python 2.6 compatible
        # Use probablepeople to tag the parts of the name.

        full_name_dict = pp.tag(fn_field)[0]

        if 'GivenName' in full_name_dict:
            # If probablepeople has successfully extracted the first name,
            # use it.
            first_name = full_name_dict['GivenName']

        if 'Surname' in full_name_dict:
            # If probablepeople has successfully extracted the surname,
            # use it.
            surname = full_name_dict['Surname']
    except (ImportError, SyntaxError, TypeError) as error:
        print(error)

    return NAMES(first_name, surname)


def get_names(fn_field):
    """
    Extract the first name and surname from a vCard 'fn' field.

    :param fn_field: the input vCard 'fn' field.
    :return: a namedtuple containing the first name and surname.

    >>> get_names('John Smith')
    Extracting data for John Smith
    Names(first_name='John', surname='Smith')
    """
    names = get_pp_names(fn_field)
    first_name = names.first_name
    surname = names.surname

    try:
        fn_field_split = fn_field.split(' ')
    except (TypeError, AttributeError):
        fn_field_split = ['']

    if first_name is None:
        # If we can't get first name from probablepeople, assume it's the
        # first part of the string.
        first_name = fn_field_split[0]
        if first_name == surname:
            first_name = ''

    if surname is None:
        # If we can't get surname from probablepeople, assume it's the
        # second part of the string, if that exists.
        if len(fn_field_split) > 1:
            surname = fn_field_split[1]
        else:
            surname = ''

    print('Extracting data for ' + first_name + ' ' + surname)

    return NAMES(first_name, surname)


def get_photo(photo):
    """
    Extract the photo data (if it exists) from a vCard 'photo' field.

    :param photo: the input vCard 'photo' field.
    :return: a base64-encoded string containing the photo data.
    """
    # TODO: Add doctest above? or pytest
    if photo is not None:
        photo_data = base64.b64encode(photo)
        photo_data = "data:image/jpeg;base64," + photo_data.decode('utf8')
    else:
        photo_data = ""

    return photo_data


def extract_contact_from_component(component):
    """
    Extract the contact info from a vCard component.

    :param component: the input vCard component text.
    :return: a dictionary containing the extracted contact info.
    """
    names = get_names(component.getChildValue('fn'))
    photo_data = get_photo(component.getChildValue('photo'))

    if photo_data == '':
        print('Warning: Missing photo for ' + names.first_name + ' ' +
              names.surname + '...!')

    entry = {'first': names.first_name, 'last': names.surname,
             'photoData': photo_data, 'details': ''}

    return entry


def extract_contacts_from_vcard(vcard):
    """
    Extract the contact info from a vCard.

    :param vcard: the vCard text to convert.
    :return: a list containing the extracted contact info.
    """
    contacts = []

    for v_component in vobject.readComponents(vcard):
        entry = extract_contact_from_component(v_component)
        contacts.append(entry)

    return contacts


def convert_to_nameshark(group_name, contacts, ):
    """
    Convert a list containing contact info into JSON for Name Shark.

    :param group_name: the Name Shark group to use.
    :param contacts:
    :return: the list containing contact info extracted from a vCard.
    """
    shark = {'name': group_name, 'contacts': contacts}
    json_str = json.dumps(shark, sort_keys=True, indent=4)

    return json_str


def vcard_to_nameshark(vcard, group_name):
    """
    Convert vCard-formatted string to the JSON format expected by Name Shark.

    :param vcard: the vCard text to convert.
    :param group_name: the Name Shark group to use.
    :return: JSON version of vCard input.
    """
    contacts = extract_contacts_from_vcard(vcard)
    json_str = convert_to_nameshark(group_name, contacts)

    return json_str


def main():
    """
    The main nameshark_vcard module.

    :return: None
    """
    # TODO: Add pytest?
    # TODO: Switch to using click, and apply click-man
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='the input file')
    parser.add_argument('group', help='the output group name')

    args = parser.parse_args()

    with open(args.file, 'r') as input_file:
        text = input_file.read()

    json_str = vcard_to_nameshark(text, args.group)

    with open(args.group + '.json', 'w') as output_file:
        output_file.write(json_str)


if __name__ == '__main__':
    main()

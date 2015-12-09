# gmail-signatures

This Python script will generate and set up Gmail signatures for multiple users.

Having a [CSV file](users.csv) with users data (name, surname, phone, etc) and a template file (see [signature-template.html](signature-template.html)) it will generate a signature file for each user.

Finally, it will use [GAM](https://github.com/jay0lee/GAM) to set up user's Gmail account to use the generated signature.

## examples

```
$ python generate-signatures.py
./generated/ethomson-signature.html
./generated/jford-signature.html
Setting Signature for ethomson@mycompany.com (1 of 1)
Setting Signature for jford@mycompany.com (1 of 1)
```

## advanced

If you need to post-process some string, you can use the modifyUsersInfo() function:

```python
users = modifyUsersInfo(users, 'phone', '(+34) %s -')
```

It will convert **666123456** into **(+34) 666123456 -**

## todo

Parameters to specify csv file, template, signatures directory, data modificators, etc...

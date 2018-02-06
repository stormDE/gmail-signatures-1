# gmail-signatures (UNMAINTAINED)

THIS PROJECT IS NOT MAINTAINED ANYMORE. GAM ADDED THE SAME FEATURE:


Signature template:
```html
<!-- signature.html -->
<!-- html signature here -->
{name} {surname}
{jobtitle}
{email}
Phone: {phone} ({extphone}) / {mobile}
```

Configure the signature to a specific user:
```
# GAM command to configure a signature to a specific user
gam user myusername@mydomain.com signature file signature.html html |
  replace name ~name \
  replace surname ~surname \
  replace jobtitle ~jobtitle \
  replace email ~email replace \
  phone ~phone replace \
  extphone ~extphone \
  replace mobile ~mobile
```

Configure the signature using a list of users:
```
# users.csv
username,name,surname,jobtitle,email,phone,extphone,mobile
jsmith, John, Smith, fsdf, jsmith@mydomain.com, 0055555, 3434, 66565656
lcroft, Lara, Croft, oeoe, lcroft@mydomain.com, 0055444, 3436, 66767857
...
```

```
# GAM command to configure a signature to a list of users from a CSV
gam csv users.csv gam user ~email signature file signature-v2.html html \
  replace name ~name \
  replace surname ~surname \
  replace jobtitle ~jobtitle \
  replace email ~email replace \
  phone ~phone replace \
  extphone ~extphone \
  replace mobile ~mobile
```

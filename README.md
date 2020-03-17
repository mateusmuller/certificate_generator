# Academics courses attendance Certificate Generator

There was a day that my girlfriend said "We created more than 100 certificates manually for each student". I said, this must be automated.

I have started to make some research about Python and how I could combine different libraries to get it done. I did it.

I have also improved the project with Docker support and other cool stuff. It was a really nice experience to learn more about automation.

## How to use it?

The goal of the script is to read a Excel sheet with the students names, generate all the certificates in PNG format and automatically send an e-mail with the attachment.

1. In order to use the script, the first step is to allow less secure apps to have access to your e-mail address, as this is a simple Python script considered a third-party and not trustable application. You can click [here](https://myaccount.google.com/lesssecureapps) and activate the option to allow less secure apps.

2. Now you can clone the repository to use it.

```
$ git clone https://github.com/mateusmuller/certificate_generator
$ cd certificate_generator
```

3. Also, you need to create a file called **credentials.json** on the same directory with this information:

```
{
    "email" : "your e-mail",
    "password" : "your password",
    "smtp_server" : "smtp.gmail.com",
    "smtp_port" : 587,
    "email_subject" : "Talk ### certificate",
    "email_body" : "Follow attached",
    "students_sheet" : "students.xlsx",
    "picture_certificate_template" : "certificate_template.png"
}
```

Change the parameters accordingly.

4. Important things to pay attention: Certificate image and Excel sheet.

* The certificate image must always be called **certificate_template.png** as it is hardcoded.
* The Excel sheet must always be called **students.xlsx** as it is hardcoded.
* The Excel sheet must always contain the same columns: (column 1 => e-mail, column 2 => full name, column 3 => the name that should be written to the certificate).
* Line 34 has the position of the text.

5. Then you can execute using Docker to automatically build the dependencies.

```
$ docker build -t certificate_generator:latest .
$ docker run --rm -v $(pwd)/credentials.json:/app/credentials.json certificate_generator:latest
```

**OBS:** I have used "-v" to pass the volume, so I don't need to rebuild the image every time I change credentials.

## Tips

I suggest to use Google Forms for the students subscription and afterwards generate an Excel sheet with all of them.

## License

See [LICENSE](LICENSE) fur further information.

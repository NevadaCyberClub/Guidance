#TO-DO: Support rich text (there's some docs on that)
#TO-DO: Ensure that template is sufficiently flexible for all guidance docs and lean more heavily on the ability to modify formatting as necessary
#TO-DO: Contingent on the above step, write comments about each field's text/size limitations
from docxtpl import DocxTemplate
import datetime
import os

Guidance_Level = "Basic"
Guidance_Category = "Device"

Path_To_Template = "/Guidance Template.docx"

if os.path.isfile(Path_To_Template) and os.access(Path_To_Template, os.R_OK):
    doc = DocxTemplate(Path_To_Template)
else:
    print("Either the file was not found or it wasn't accesible. Program exiting...")

context = {
    # Level (1 capital letter)
    "L" : Guidance_Level[0],
    # Help category (Device, Data, or Identiy)
    "type" : Guidance_Category,
    #
    "why_it_matters" : "Consider how much yodatetime and how disruptive and damaging it would be to break, lose, or have your device stolen. You quickly readatetimethe information on a typical smartphone, all the access it provides to communications (phone, text, e-mail), and as an alternative form of payment, it is important to protect your smartphone from unauthorized use. Protecting your device involves locking it to prevent unauthorized access, using antivirus software to protect against malware (malicious software), being familiar with the security settings of your device, and recovering if your device is damaged, lost or stolen.",
    #
    "what_to_know" : "Anyone can access an unlocked device, which means anyone can access your pictures, videos, and apps. Locking your phone is like adding a \"gatekeeper\" to your device, keeping it secure against unauthorized access. Setting a passcode means anyone trying to access your device has to enter a PIN or passcode to unlock it. You can also set your device to lock itself after being inactive for a specific amount of time. Antivirus software is the \"policeman\" at the gate of a computer system. It protects the computer from incoming threats and seeks out, destroys and warns of possible threats to the system.",
    #
    "what_to_do_head_1" : "Lock your device. The longer and more complex the passcode, the more difficult it will be to guess or \"hack\". This makes it harder for someone to gain unauthorized access to your device.",
    #
    "what_to_do_1_1" : "\"Why Smartphone Owners Won't Use Lock Screens\" - Tom's Guide",
    #
    "what_to_do_1_2" : "http://www.tomsguide.com/us/smartphone-lock-screenrefusal,news-19875.html",
    #
    "what_to_do_head_2" : "Install Anti-Virus software. Trojans, botnets, ransomware, rootkits - antivirus utilities protect against all kinds of malware, not just viruses. Antivirus protection is critical. There are many anti-virus applications available for the Android and iOS smartphones. Once you download and install anti-virus software it will automatically begin to protect your device.",
    #
    "what_to_do_2_1" : "\"Why You Need Antivirus Software\" - PC Magazine",
    #
    "what_to_do_2_2" : "http://securitywatch.pcmag.com/securitysoftware/330459-why-you-need-antivirus-software",
    #
    "how_to_do_it_head_1" : "LOCK SCREEN",
    #
    "how_to_do_it_1_1" : "Android: You can use a pattern, 4+ digit pin, or alphanumeric password for android screen lock functionality.",
    #
    "how_to_do_it_1_2" : "iOS: You can use a 4+ digit pin or alphanumeric password for iOS screen lock functionality.",
    #
    "how_to_do_it_2_1" : "http://www.howtogeek.com/253101/how-to-secureyour-android-phone-with-a-pin-password-or-pattern/",
    #
    "how_to_do_it_2_2" : "https://support.apple.com/en-us/HT204060",
    #
    "how_to_do_it_head_2" : "ANTI-VIRUS",
    #
    "how_to_do_it_3_1" : "Android: Evaluate and install antivirus software.",
    #
    "how_to_do_it_3_2" : "iOS: Evaluate and install antivirus software.",
    #
    "how_to_do_it_4_1" : "https://www.av-test.org/en/antivirus/",
    #
    "how_to_do_it_4_2" : "http://www.alltechfeed.com/best-antivirus-iphone-ipad2016/",
    #
    "disclaimer" : "WARNING: Changes to device and application settings can have unintended consequences and may interfere with normal operation. Improper use of encryption and authentication can cause a loss of data and prevent access. Please do not attempt to apply any guidance that exceeds your level of knowledge and familiarity with your device or application. All guidance is provided \"as-is\" from referenced sources. User assumes responsibility for any changes made to their device and/or applications.",
    #
    "footer" : Guidance_Category.upper() + "-" + Guidance_Level,
    #
    "up_date" : str(datetime.date.today()),
}

doc.render(context)

doc.save(Guidance_Category + "_" + Guidance_Level + ".docx")
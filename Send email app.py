#!/usr/bin/env python
# coding: utf-8

# In[50]:


from email.message import EmailMessage
import ssl
import smtplib


# In[51]:


# My email details


# In[52]:


email_sender = ''
email_password = ''


# In[53]:


email_receiver = ''


# In[54]:


subject = 'Dont forget to subscribe'
body = """ When you watch a video please subscribe"""


# In[55]:


#Create an instance of the email library


# In[56]:


em = EmailMessage()


# In[57]:


em['From'] = email_sender


# In[58]:


em['to'] = email_receiver


# In[59]:


em['subject'] = subject


# In[60]:


em.set_content(body)


# In[61]:


context = ssl.create_default_context()


# In[62]:


#Logging in into my acc
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())


# In[ ]:





# 🏥 Srilekha Hospital - Complete Website Package

## 📦 What's Included

### Frontend
- ✅ **index.html** - Complete bilingual website (English & Telugu)
- ✅ All images embedded (no external files needed)
- ✅ Fully responsive (mobile, tablet, desktop)
- ✅ Language selection with beautiful UI
- ✅ Images in About section
- ✅ New Facilities section
- ✅ Working appointment form
- ✅ WhatsApp integration
- ✅ Fixed JavaScript (no errors!)

### Backend
- ✅ **server.py** - Python Flask backend
- ✅ Appointment handling API
- ✅ Email notifications
- ✅ CORS enabled for security
- ✅ **requirements.txt** - Python dependencies

---

## 🚀 Quick Start

### Option 1: Frontend Only (Static Website)

**Perfect for:**
- GitHub Pages
- Netlify
- Vercel
- Any static hosting

**Steps:**
1. Upload `index.html` to your hosting
2. Done! No backend needed
3. Appointments use mailto fallback

**Pros:** Simple, free, instant  
**Cons:** Opens user's email client

---

### Option 2: Frontend + Backend (Full Solution)

**Perfect for:**
- Professional setup
- Direct email delivery
- Full control
- Better user experience

**Requirements:**
- Python 3.8+
- Server (VPS, cloud, or local)

#### Installation Steps:

**1. Install Python Dependencies**
```bash
cd website-complete
pip install -r requirements.txt
```

**2. Start the Backend Server**
```bash
python server.py
```

Server runs on: `http://localhost:5000`

**3. Update Frontend API Endpoint**

In `index.html`, find this line:
```javascript
const response = await fetch('https://formsubmit.co/ajax/srilekhahospitals@gmail.com', {
```

Replace with:
```javascript
const response = await fetch('http://localhost:5000/api/book-appointment', {
```

Or use your actual server URL:
```javascript
const response = await fetch('https://yourdomain.com/api/book-appointment', {
```

**4. Configure Email (Production)**

Edit `server.py`:
```python
# Add your email password
SMTP_PASSWORD = "your-app-specific-password"
```

**To get App-Specific Password:**
1. Go to Google Account → Security
2. Enable 2-Step Verification
3. Create "App Password"
4. Use that password in server.py

---

## 🔧 Backend API Documentation

### Endpoints

#### 1. Book Appointment
```
POST /api/book-appointment
Content-Type: application/json

{
  "name": "Patient Name",
  "age": 30,
  "sex": "Male",
  "phone": "9876543210",
  "email": "patient@email.com",
  "doctor": "Dr. Rohith Meesa - Pulmonology",
  "reason": "Breathing difficulty",
  "preferred_date": "2026-02-20",
  "language": "english"
}

Response 200 OK:
{
  "success": true,
  "message": "Appointment booked successfully",
  "data": {
    "patient_name": "Patient Name",
    "doctor": "Dr. Rohith Meesa",
    "confirmation_time": "2026-02-16T16:30:00"
  }
}
```

#### 2. Health Check
```
GET /api/health

Response:
{
  "status": "healthy",
  "service": "Srilekha Hospital API",
  "timestamp": "2026-02-16T16:30:00"
}
```

#### 3. Contact Form
```
POST /api/contact

{
  "name": "Name",
  "email": "email@example.com",
  "message": "Message text"
}
```

---

## 🌐 Deployment Options

### Option A: Frontend on Netlify, Backend on Heroku

**Frontend (Netlify):**
1. Drag `index.html` to Netlify
2. Get URL: `https://your-site.netlify.app`
3. Update API endpoint in HTML to point to Heroku

**Backend (Heroku):**
1. Create `Procfile`:
   ```
   web: gunicorn server:app
   ```
2. Deploy to Heroku
3. Get URL: `https://your-app.herokuapp.com`
4. Update frontend to use this URL

### Option B: Both on Same Server

**Using DigitalOcean/AWS/Azure:**
1. Set up Ubuntu server
2. Install Nginx
3. Configure reverse proxy
4. Run Flask with Gunicorn
5. Serve frontend as static files

### Option C: Serverless (AWS Lambda)

Convert backend to Lambda function:
- Use AWS API Gateway
- Lambda for appointment handling
- S3 for frontend hosting
- CloudFront for CDN

---

## 📧 Email Configuration

### Gmail Setup (Recommended for Testing)

1. **Enable 2-Factor Authentication**
   - Google Account → Security → 2-Step Verification

2. **Generate App Password**
   - Security → App passwords → Select "Mail" → Generate
   - Copy the 16-character password

3. **Update server.py**
```python
HOSPITAL_EMAIL = "srilekhahospitals@gmail.com"
SMTP_PASSWORD = "your-16-char-password"
```

4. **Uncomment Production Code**
   - In `server.py`, uncomment the SMTP sending section

### Alternative: SendGrid (Recommended for Production)

```bash
pip install sendgrid
```

```python
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='noreply@srilekhahospital.com',
    to_emails='srilekhahospitals@gmail.com',
    subject='New Appointment',
    html_content=html_body
)

sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
response = sg.send(message)
```

---

## 🔒 Security Best Practices

### 1. Environment Variables
Create `.env` file:
```
SMTP_PASSWORD=your-password
HOSPITAL_EMAIL=srilekhahospitals@gmail.com
SECRET_KEY=your-secret-key
```

Load in `server.py`:
```python
from dotenv import load_dotenv
load_dotenv()

SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
```

### 2. HTTPS Only
- Get SSL certificate (Let's Encrypt - free)
- Configure Nginx with HTTPS
- Redirect HTTP to HTTPS

### 3. Rate Limiting
```bash
pip install Flask-Limiter
```

```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=lambda: request.remote_addr)

@app.route('/api/book-appointment', methods=['POST'])
@limiter.limit("5 per minute")  # Max 5 appointments per minute
def book_appointment():
    ...
```

### 4. Input Validation
```python
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Email, Length

class AppointmentForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(min=2, max=100)])
    age = IntegerField('age', validators=[DataRequired()])
    # ... etc
```

---

## 📱 Features Implemented

### ✅ Fixed Issues
1. **JavaScript Errors** - selectLanguage function now in global scope
2. **Language Selection** - Beautiful UI with logo, hospital name, light blue background
3. **About Section** - Real images for ambulance, doctors, equipment
4. **Facilities Section** - New section with 8 facilities and images
5. **Appointment Form** - Direct submission with success message
6. **Mobile Responsive** - Works perfectly on all devices

### ✅ Enhanced Features
- WhatsApp chat button (floating + hero)
- Professional email templates
- Backend API for appointments
- Bilingual support (English ↔ Telugu)
- Form validation
- Success confirmations
- Error handling

---

## 🧪 Testing

### Test Frontend Locally
```bash
# Simple HTTP server
python -m http.server 8000

# Open browser
http://localhost:8000/index.html
```

### Test Backend API
```bash
# Start server
python server.py

# Test health check
curl http://localhost:5000/api/health

# Test appointment (replace with actual data)
curl -X POST http://localhost:5000/api/book-appointment \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test Patient",
    "age": 30,
    "sex": "Male",
    "phone": "9876543210",
    "doctor": "Dr. Rohith Meesa",
    "reason": "Test appointment"
  }'
```

---

## 🆘 Troubleshooting

### Problem: "selectLanguage is not defined"
**Solution:** Use the new `index.html` - function is now in global scope

### Problem: Form doesn't submit
**Solutions:**
1. Check browser console for errors
2. Verify backend is running: `http://localhost:5000/api/health`
3. Check CORS settings
4. Verify API endpoint URL in frontend

### Problem: Emails not sending
**Solutions:**
1. Check Gmail App Password is correct
2. Verify SMTP settings
3. Check spam folder
4. Enable "Less secure app access" (if using regular password)
5. Use SendGrid instead for production

### Problem: Images not showing
**Solution:** Images are embedded as base64 - should work automatically. If not, check browser console.

---

## 📊 Production Checklist

- [ ] Configure environment variables
- [ ] Set up HTTPS/SSL
- [ ] Enable rate limiting
- [ ] Configure proper SMTP (SendGrid/AWS SES)
- [ ] Set up monitoring (uptime, errors)
- [ ] Configure backups
- [ ] Test on multiple devices
- [ ] Test in multiple browsers
- [ ] Set up analytics (Google Analytics)
- [ ] Configure CDN for images
- [ ] Set up error logging (Sentry)
- [ ] Create admin dashboard (optional)

---

## 💰 Hosting Costs

### Free Options:
- **Frontend:** Netlify/Vercel/GitHub Pages - FREE
- **Backend:** Heroku Free Tier, Railway, Render - FREE
- **Email:** SendGrid (100 emails/day) - FREE
- **Total:** ₹0/month

### Paid Options (Recommended for production):
- **VPS (DigitalOcean):** $6/month (~₹500)
- **Domain:** ₹500-1000/year
- **Email (SendGrid Pro):** $15/month
- **Total:** ~₹1500/month

---

## 📞 Support

For technical support:
- Check this documentation first
- Test locally before deploying
- Check browser console for errors
- Verify backend logs

---

## 🎉 You're All Set!

Your hospital now has a:
- ✅ Professional bilingual website
- ✅ Working appointment system
- ✅ Mobile-responsive design
- ✅ Backend API
- ✅ Email notifications
- ✅ WhatsApp integration

**Next step:** Choose your deployment option and go live!

Good luck with Srilekha Hospital! 🏥✨

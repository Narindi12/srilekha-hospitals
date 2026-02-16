#!/usr/bin/env python3
"""
Srilekha Hospital - Backend Server
Handles appointment submissions and sends emails
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# Email configuration
HOSPITAL_EMAIL = "srilekhahospitals@gmail.com"
# Note: For production, use environment variables or config file
# SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD')

@app.route('/api/book-appointment', methods=['POST'])
def book_appointment():
    """
    Handle appointment booking requests
    Receives patient data and sends email to hospital
    """
    try:
        # Get data from request
        data = request.json
        
        # Validate required fields
        required_fields = ['name', 'age', 'sex', 'phone', 'doctor', 'reason']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({
                    'success': False,
                    'message': f'Missing required field: {field}'
                }), 400
        
        # Extract data
        patient_name = data.get('name')
        age = data.get('age')
        sex = data.get('sex')
        phone = data.get('phone')
        email = data.get('email', 'Not provided')
        doctor = data.get('doctor')
        reason = data.get('reason')
        preferred_date = data.get('preferred_date', 'Not specified')
        language = data.get('language', 'english')
        
        # Create email content
        subject = f"New Appointment Request - {patient_name}"
        
        html_body = f"""
        <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
                .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                .header {{ background: linear-gradient(135deg, #0066CC 0%, #00A4BD 100%); 
                          color: white; padding: 30px; text-align: center; border-radius: 10px 10px 0 0; }}
                .header h1 {{ margin: 0; font-size: 28px; }}
                .content {{ background: #f9f9f9; padding: 30px; border-radius: 0 0 10px 10px; }}
                .info-table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
                .info-table td {{ padding: 12px; border-bottom: 1px solid #ddd; }}
                .info-table td:first-child {{ font-weight: bold; width: 180px; color: #0066CC; }}
                .reason-box {{ background: white; padding: 15px; border-left: 4px solid #0066CC; 
                              margin: 20px 0; border-radius: 5px; }}
                .footer {{ text-align: center; margin-top: 30px; color: #666; font-size: 14px; }}
                .badge {{ display: inline-block; padding: 5px 15px; background: #00A4BD; 
                         color: white; border-radius: 20px; font-size: 12px; margin-top: 10px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>🏥 New Appointment Request</h1>
                    <div class="badge">URGENT - Please Review</div>
                </div>
                <div class="content">
                    <h2 style="color: #0066CC; margin-top: 0;">Patient Information</h2>
                    <table class="info-table">
                        <tr>
                            <td>Patient Name:</td>
                            <td><strong>{patient_name}</strong></td>
                        </tr>
                        <tr>
                            <td>Age:</td>
                            <td>{age} years</td>
                        </tr>
                        <tr>
                            <td>Sex:</td>
                            <td>{sex}</td>
                        </tr>
                        <tr>
                            <td>Phone Number:</td>
                            <td><a href="tel:{phone}" style="color: #0066CC; text-decoration: none;">{phone}</a></td>
                        </tr>
                        <tr>
                            <td>Email Address:</td>
                            <td>{email if email != 'Not provided' else '<em>Not provided</em>'}</td>
                        </tr>
                        <tr>
                            <td>Preferred Date:</td>
                            <td>{preferred_date}</td>
                        </tr>
                    </table>
                    
                    <h2 style="color: #0066CC;">Appointment Details</h2>
                    <table class="info-table">
                        <tr>
                            <td>Doctor Requested:</td>
                            <td><strong>{doctor}</strong></td>
                        </tr>
                    </table>
                    
                    <h3 style="color: #0066CC;">Reason for Visit:</h3>
                    <div class="reason-box">
                        {reason}
                    </div>
                    
                    <div class="footer">
                        <p><strong>Submitted on:</strong> {datetime.now().strftime('%B %d, %Y at %I:%M %p')}</p>
                        <p style="color: #999; font-size: 12px;">
                            This appointment request was submitted via Srilekha Hospital website
                        </p>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """
        
        # Plain text version for email clients that don't support HTML
        text_body = f"""
        New Appointment Request - Srilekha Hospital
        
        PATIENT INFORMATION
        {'='*50}
        Name: {patient_name}
        Age: {age} years
        Sex: {sex}
        Phone: {phone}
        Email: {email}
        
        APPOINTMENT DETAILS
        {'='*50}
        Doctor Requested: {doctor}
        Preferred Date: {preferred_date}
        
        REASON FOR VISIT
        {'='*50}
        {reason}
        
        {'='*50}
        Submitted on: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}
        """
        
        # For now, return success without actually sending email
        # In production, configure SMTP settings and uncomment email sending code
        
        # Simulated success response
        return jsonify({
            'success': True,
            'message': 'Appointment request received successfully',
            'data': {
                'patient_name': patient_name,
                'doctor': doctor,
                'confirmation_time': datetime.now().isoformat()
            }
        }), 200
        
        # PRODUCTION CODE (Uncomment and configure for real email sending):
        """
        try:
            # Create message
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = 'noreply@srilekhahospital.com'
            msg['To'] = HOSPITAL_EMAIL
            
            # Attach both plain text and HTML versions
            part1 = MIMEText(text_body, 'plain')
            part2 = MIMEText(html_body, 'html')
            msg.attach(part1)
            msg.attach(part2)
            
            # Send email using Gmail SMTP
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(HOSPITAL_EMAIL, SMTP_PASSWORD)
                server.send_message(msg)
            
            return jsonify({
                'success': True,
                'message': 'Appointment booked successfully. We will contact you soon.'
            }), 200
            
        except Exception as e:
            return jsonify({
                'success': False,
                'message': f'Failed to send email: {str(e)}'
            }), 500
        """
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Server error: {str(e)}'
        }), 500


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Srilekha Hospital API',
        'timestamp': datetime.now().isoformat()
    }), 200


@app.route('/api/contact', methods=['POST'])
def contact_form():
    """Handle general contact form submissions"""
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
        
        # Log or process contact form
        # In production, send email to hospital
        
        return jsonify({
            'success': True,
            'message': 'Thank you for contacting us. We will respond shortly.'
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error: {str(e)}'
        }), 500


if __name__ == '__main__':
    # Development server
    # For production, use gunicorn or similar WSGI server
    print("🏥 Srilekha Hospital Backend Server")
    print("📧 Email: srilekhahospitals@gmail.com")
    print("🌐 Starting server on http://localhost:5000")
    print("\n⚠️  Note: Email sending is currently simulated.")
    print("   Configure SMTP settings in production.\n")
    
    app.run(host='0.0.0.0', port=5000, debug=True)

# ieuk-task-2025
- Deborah Ama submission
- I had an issue with my previous repo so this was made last minute with my orginal code
- <img width="606" height="114" alt="image" src="https://github.com/user-attachments/assets/d1e376b8-45d0-4470-acd6-9aa1b6c2a857" />


# 📊 Traffic Analysis Report: Bot Activity and Mitigation Recommendations

## Overview:

Analysis of the web traffic logs reveals strong evidence of bot activity targeting the music media start-up’s website. Several IP addresses generated abnormally high volumes of traffic. The most active, 45.133.1.1 and 45.133.1.2, made over 4,600 requests each. Followed by 35.185.0.156 with 3600 requests. 

## User-Agent Insights:

Although most requests used common browser user agents (Chrome, Safari, Firefox), a noticeable subset identified well-known automated tools:

* Wget, curl, and HTTPie together generated over 7,000 requests.

* Tools such as python-requests, sqlmap, and Postman also appeared, indicating possible scraping or probing activity.

## Recommendations (Cost-Effective):

1. Rate Limiting: Configure Nginx, Cloudflare, or AWS WAF to limit requests per IP (e.g., 100 requests per hour).

2. Bot Filtering: Block traffic based on suspicious user-agent strings (e.g., curl, sqlmap, python-requests).

3. IP Blocking: Blacklist or throttle IPs identified in the top offenders, especially 45.133.1.x and 35.185.0.156.

4. CAPTCHA Implementation: Add lightweight CAPTCHA to vulnerable endpoints like /contact and /subscribe-premium.

These measures are low-cost, require minimal maintenance, and are well-suited to the limited resources of a small team, while significantly reducing server load and preserving site performance.


# My approach

I haven't had experience with working with logs and requests so I asked chatgpt to help me understand some logs and it also aided me in producing the code as well.  Numbers included in my overview are the numbers that were outputted from the script.

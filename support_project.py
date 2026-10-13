# AI Support Copilot
# Built by Simrandeep Kaur

def determine_priority(ticket):
    ticket_lower = ticket.lower()

    if "production is completely down" in ticket_lower or "all customers" in ticket_lower:
        return "P1"

    elif "workaround" in ticket_lower or "one user" in ticket_lower:
        return "P3"

    elif "blocked" in ticket_lower or "unable to" in ticket_lower:
        return "P2"

    else:
        return "P4"

def analyze_ticket(ticket):
    priority = determine_priority(ticket)

    if "401" in ticket or "token" in ticket.lower():
        category = "API Authentication"
        reason = "Authentication failure may be blocking API access."
        missing_info = "Request ID, timestamp, endpoint, and token scope."
        next_step = "Verify authentication settings and review API logs."

    elif "saml" in ticket.lower() or "sso" in ticket.lower():
        category = "SSO / SAML"
        reason = "Users may be unable to authenticate through SSO."
        missing_info = "Affected users, timestamp, IdP, and exact error."
        next_step = "Check SAML configuration and certificate status."

    elif "import" in ticket.lower() or "records" in ticket.lower():
        category = "Data / Integration"
        reason = "Expected data may be missing after processing."
        missing_info = "Job ID, timestamp, file name, and record count."
        next_step = "Check ingestion status and downstream processing logs."
    elif "how to" in ticket.lower() or "how do i" in ticket.lower():
        category = "Informational / How-To"
        reason = "Customer is requesting product guidance."
        missing_info = "Specific feature or workflow the customer needs help with."
        next_step = "Provide the relevant instructions or knowledge base article."
    else:
        category = "Unknown"
        reason = "More investigation is required."
        missing_info = "Error message, timestamp, impact, and recent changes."
        next_step = "Gather additional diagnostic information."

    return {
        "category": category,
        "priority": priority,
        "reason": reason,
        "missing_info": missing_info,
        "next_step": next_step
    }

ticket = input("Enter the customer support ticket: ")

result = analyze_ticket(ticket)

print()
print("AI Support Copilot")
print("------------------")
print("Category:", result["category"])
print("Priority:", result["priority"])
print("Reason:", result["reason"])
print("Missing Information:", result["missing_info"])
print("Next Step:", result["next_step"])

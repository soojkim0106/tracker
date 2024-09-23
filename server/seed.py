from app import app
from config import db
from models.task import Task

with app.app_context():
    Task.query.delete()
    print("Deleted all tasks")

    task1 = Task(
        title="Organize Office Desk",
        description="Clean and rearrange the desk, organize files, and declutter the workspace.",
        status="Not Started",
    )

    task2 = Task(
        title="Finish Budget Report",
        description="Complete the monthly budget report and send it to the finance department.",
        status="In Progress",
    )

    task3 = Task(
        title="Call Supplier for Order Update",
        description="Contact the supplier to confirm the status of the recent shipment.",
        status="Completed",
    )

    task4 = Task(
        title="Plan Team Meeting",
        description="Schedule and organize the agenda for next week's team meeting.",
        status="Not Started",
    )

    task5 = Task(
        title="Update Project Documentation",
        description="Review and revise the documentation for the ongoing project.",
        status="In Progress",
    )

    task6 = Task(
        title="Submit Quarterly Sales Data",
        description="Prepare and submit sales figures for the last quarter.",
        status="Completed",
    )

    task7 = Task(
        title="Design Marketing Campaign",
        description="Develop a concept for the new social media marketing campaign.",
        status="Not Started",
    )

    task8 = Task(
        title="Conduct User Interviews",
        description="Set up interviews with five users to gather feedback for the new product.",
        status="In Progress",
    )

    task9 = Task(
        title="Review Annual Goals",
        description="Analyze the progress on yearly goals and prepare a report.",
        status="Completed",
    )

    task10 = Task(
        title="Update Software",
        description="Install the latest software updates across all company devices.",
        status="Not Started",
    )

    task11 = Task(
        title="Hire New Intern",
        description="Post job listings and interview candidates for the internship position.",
        status="In Progress",
    )

    task12 = Task(
        title="Draft Blog Post",
        description="Write a draft for the upcoming blog post on product features.",
        status="Completed",
    )

    task13 = Task(
        title="Research Competitor Products",
        description="Analyze competitor products and prepare a comparison chart.",
        status="Not Started",
    )

    task14 = Task(
        title="Set Up Client Presentation",
        description="Organize the slide deck and presentation for the client meeting next week.",
        status="In Progress",
    )

    task15 = Task(
        title="Finalize Event Venue",
        description="Confirm the booking for the annual company event.",
        status="Completed",
    )

    task16 = Task(
        title="Test New Software Features",
        description="Run tests on the newly implemented software features and record results.",
        status="Not Started",
    )

    task17 = Task(
        title="Update Employee Records",
        description="Ensure all employee records are up-to-date in the HR system.",
        status="In Progress",
    )

    task18 = Task(
        title="Send Invitations for Webinar",
        description="Send email invitations to prospective attendees for the upcoming webinar.",
        status="Completed",
    )

    task19 = Task(
        title="Review Performance Feedback",
        description="Go through recent performance reviews and compile a summary.",
        status="Not Started",
    )

    task20 = Task(
        title="Plan Q4 Strategy",
        description="Develop and outline the business strategy for the next quarter.",
        status="In Progress",
    )


    tasks = [task1, task2, task3, task4, task5, task6, task7, task8, task9, task10, task11, task12, task13, task14, task15, task16, task17, task18, task19, task20]

    db.session.add_all(tasks)
    db.session.commit()

    print("Added task")

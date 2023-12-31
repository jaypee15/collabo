# Generated by Django 4.2.6 on 2023-10-08 19:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tags",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("Frontend", "Frontend"),
                            ("Backend", "Backend"),
                            ("Full Stack", "Full Stack"),
                            ("Mobile App", "Mobile App"),
                            ("Responsive Design", "Responsive Design"),
                            ("User Interface", "User Interface"),
                            ("User Experience", "User Experience"),
                            ("Database", "Database"),
                            ("API Development", "API Development"),
                            ("Testing", "Testing"),
                            ("Deployment", "Deployment"),
                            ("Version Control", "Version Control"),
                            ("Web Security", "Web Security"),
                            ("Data Analysis", "Data Analysis"),
                            ("Machine Learning", "Machine Learning"),
                            ("Artificial Intelligence", "Artificial Intelligence"),
                            ("Cloud Computing", "Cloud Computing"),
                            ("DevOps", "DevOps"),
                            ("Blockchain", "Blockchain"),
                            ("Internet of Things", "Internet of Things"),
                            ("Game Development", "Game Development"),
                            ("Open Source", "Open Source"),
                            ("Community", "Community"),
                            ("Education", "Education"),
                            ("Finance", "Finance"),
                            ("Healthcare", "Healthcare"),
                            ("E-commerce", "E-commerce"),
                            ("Social Networking", "Social Networking"),
                            ("Non-profit", "Non-profit"),
                            ("Startups", "Startups"),
                            ("Research", "Research"),
                            ("Design Patterns", "Design Patterns"),
                            ("Agile", "Agile"),
                            ("Scrum", "Scrum"),
                            ("Kanban", "Kanban"),
                            ("Project Management", "Project Management"),
                            ("Remote Work", "Remote Work"),
                            ("Freelancing", "Freelancing"),
                            ("Coding Standards", "Coding Standards"),
                            ("UI Frameworks", "UI Frameworks"),
                            ("Serverless", "Serverless"),
                            ("Data Visualization", "Data Visualization"),
                            ("AI Ethics", "AI Ethics"),
                            ("Accessibility", "Accessibility"),
                            ("Gaming Engines", "Gaming Engines"),
                            ("VR/AR Development", "VR/AR Development"),
                            ("Robotics", "Robotics"),
                            ("Bioinformatics", "Bioinformatics"),
                            ("Music Production", "Music Production"),
                            ("Photography", "Photography"),
                            ("Video Editing", "Video Editing"),
                            ("Blogging", "Blogging"),
                            ("Graphic Design", "Graphic Design"),
                            ("Content Marketing", "Content Marketing"),
                            ("SEO", "SEO"),
                            ("Digital Marketing", "Digital Marketing"),
                            ("Cryptocurrency", "Cryptocurrency"),
                            ("AI Chatbots", "AI Chatbots"),
                            ("Legal Tech", "Legal Tech"),
                            ("Fashion Tech", "Fashion Tech"),
                            ("Food Tech", "Food Tech"),
                            ("Travel Tech", "Travel Tech"),
                            ("Sports Tech", "Sports Tech"),
                            ("Other", "Other"),
                        ],
                        max_length=100,
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="project",
            name="tags",
        ),
        migrations.AddField(
            model_name="project",
            name="tags",
            field=models.ManyToManyField(related_name="project_tags", to="projects.tags", verbose_name="Project tags"),
        ),
    ]

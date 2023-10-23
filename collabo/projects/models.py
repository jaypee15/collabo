import uuid
from django.db  import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.urls import reverse


User = settings.AUTH_USER_MODEL

class Skill(models.Model):

        SKILL_CHOICES = (
            ('JavaScript', 'JavaScript'),
            ('Python', 'Python'),
            ('HTML/CSS', 'HTML/CSS'),
            ('React', 'React'),
            ('Angular', 'Angular'),
            ('Vue.js', 'Vue.js'),
            ('Node.js', 'Node.js'),
            ('Express.js', 'Express.js'),
            ('Ruby', 'Ruby'),
            ('Ruby on Rails', 'Ruby on Rails'),
            ('Java', 'Java'),
            ('Spring Boot', 'Spring Boot'),
            ('C#', 'C#'),
            ('ASP.NET', 'ASP.NET'),
            ('PHP', 'PHP'),
            ('Laravel', 'Laravel'),
            ('Django', 'Django'),
            ('Flask', 'Flask'),
            ('SQL', 'SQL'),
            ('NoSQL', 'NoSQL'),
            ('Git', 'Git'),
            ('REST API', 'REST API'),
            ('GraphQL', 'GraphQL'),
            ('Responsive Web Design', 'Responsive Web Design'),
            ('UI/UX Design', 'UI/UX Design'),
            ('Wireframing', 'Wireframing'),
            ('Adobe Creative Suite', 'Adobe Creative Suite'),
            ('DevOps', 'DevOps'),
            ('Containerization (Docker)', 'Containerization (Docker)'),
            ('Cloud Computing (AWS, Azure, GCP)', 'Cloud Computing (AWS, Azure, GCP)'),
            ('Cybersecurity', 'Cybersecurity'),
            ('Machine Learning', 'Machine Learning'),
            ('Data Analysis', 'Data Analysis'),
            ('Agile Development', 'Agile Development'),
            ('Project Management', 'Project Management'),
            # Add more skills as needed
        )



        name = models.CharField(max_length=100, choices = SKILL_CHOICES)

        def __str__(self) -> str:
             return self.name
        
class Tags(models.Model):


    PROJECT_TAG_CHOICES = (
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend'),
        ('Full Stack', 'Full Stack'),
        ('Mobile App', 'Mobile App'),
        ('Responsive Design', 'Responsive Design'),
        ('User Interface', 'User Interface'),
        ('User Experience', 'User Experience'),
        ('Database', 'Database'),
        ('API Development', 'API Development'),
        ('Testing', 'Testing'),
        ('Deployment', 'Deployment'),
        ('Version Control', 'Version Control'),
        ('Web Security', 'Web Security'),
        ('Data Analysis', 'Data Analysis'),
        ('Machine Learning', 'Machine Learning'),
        ('Artificial Intelligence', 'Artificial Intelligence'),
        ('Cloud Computing', 'Cloud Computing'),
        ('DevOps', 'DevOps'),
        ('Blockchain', 'Blockchain'),
        ('Internet of Things', 'Internet of Things'),
        ('Game Development', 'Game Development'),
        ('Open Source', 'Open Source'),
        ('Community', 'Community'),
        ('Education', 'Education'),
        ('Finance', 'Finance'),
        ('Healthcare', 'Healthcare'),
        ('E-commerce', 'E-commerce'),
        ('Social Networking', 'Social Networking'),
        ('Non-profit', 'Non-profit'),
        ('Startups', 'Startups'),
        ('Research', 'Research'),
        ('Design Patterns', 'Design Patterns'),
        ('Agile', 'Agile'),
        ('Scrum', 'Scrum'),
        ('Kanban', 'Kanban'),
        ('Project Management', 'Project Management'),
        ('Remote Work', 'Remote Work'),
        ('Freelancing', 'Freelancing'),
        ('Coding Standards', 'Coding Standards'),
        ('UI Frameworks', 'UI Frameworks'),
        ('Serverless', 'Serverless'),
        ('Data Visualization', 'Data Visualization'),
        ('AI Ethics', 'AI Ethics'),
        ('Accessibility', 'Accessibility'),
        ('Gaming Engines', 'Gaming Engines'),
        ('VR/AR Development', 'VR/AR Development'),
        ('Robotics', 'Robotics'),
        ('Bioinformatics', 'Bioinformatics'),
        ('Music Production', 'Music Production'),
        ('Photography', 'Photography'),
        ('Video Editing', 'Video Editing'),
        ('Blogging', 'Blogging'),
        ('Graphic Design', 'Graphic Design'),
        ('Content Marketing', 'Content Marketing'),
        ('SEO', 'SEO'),
        ('Digital Marketing', 'Digital Marketing'),
        ('Cryptocurrency', 'Cryptocurrency'),
        ('AI Chatbots', 'AI Chatbots'),
        ('Legal Tech', 'Legal Tech'),
        ('Fashion Tech', 'Fashion Tech'),
        ('Food Tech', 'Food Tech'),
        ('Travel Tech', 'Travel Tech'),
        ('Sports Tech', 'Sports Tech'),
        ('Other', 'Other'),
        # Add more tags as needed
    )
    name = models.CharField(max_length=100, choices=PROJECT_TAG_CHOICES)


    def __str__(self):
        return self.name

        

class Project(models.Model):

    """
    custom model for listing a project that requires collaboration.
   
    """

    PROJECT_CATEGORY_CHOICES = (
        ('Web Development', 'Web Development'),
        ('Mobile App Development', 'Mobile App Development'),
        ('Data Science', 'Data Science'),
        ('Machine Learning', 'Machine Learning'),
        ('Artificial Intelligence', 'Artificial Intelligence'),
        ('UI/UX Design', 'UI/UX Design'),
        ('Graphic Design', 'Graphic Design'),
        ('Game Development', 'Game Development'),
        ('DevOps', 'DevOps'),
        ('Cloud Computing', 'Cloud Computing'),
        ('Cybersecurity', 'Cybersecurity'),
        ('IoT (Internet of Things)', 'IoT (Internet of Things)'),
        ('Blockchain', 'Blockchain'),
        ('AR/VR (Augmented Reality/Virtual Reality)', 'AR/VR (Augmented Reality/Virtual Reality)'),
        ('E-commerce', 'E-commerce'),
        ('Social Networking', 'Social Networking'),
        ('Education', 'Education'),
        ('Healthcare', 'Healthcare'),
        ('Finance', 'Finance'),
        ('Non-profit', 'Non-profit'),
        ('Open Source', 'Open Source'),
        ('Other', 'Other'),
        # Add more categories as needed
    )


    
    
    PROJECT_STATUS_CHOICES = (
        ('Planning', 'Planning'),
        ('In Progress', 'In Progress'),
        ('On Hold', 'On Hold'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
        ('Archived', 'Archived'),
        ('Other', 'Other'),
    )


    id = models.CharField(primary_key=True,
                           default=uuid.uuid4, editable=False, max_length=36)
    title = models.CharField(_("Name of project"), max_length=200)
    description = models.TextField(_("project description"), )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Project Creator"))
    collaborators = models.ManyToManyField( User, related_name="project_collaborators", blank=True, verbose_name=_("Project collaborators"),)
    skills_required = models.ManyToManyField(Skill, related_name="required_skills", verbose_name=_("Skills required from collaborators"))
    created_at = models.DateTimeField(_("Time of project creation"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Last Modification time"), auto_now=True)
    is_active = models.BooleanField(_("Is project still ongoing?"), default=True)
    is_accepting_collaborators = models.BooleanField(_("Is project still looking for collaborators?"), default=True)
    category = models.CharField(max_length=100, choices=PROJECT_CATEGORY_CHOICES)
    tags = models.ManyToManyField(Tags, related_name="project_tags", verbose_name=_("Project tags"))
    project_status = models.CharField(max_length=20, choices=PROJECT_STATUS_CHOICES, default='Planning')
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()

    def __str__(self) -> str:
        return f"{self.title} by {self.created_by} at {self.created_at}"

    def get_absolute_url(self) -> str:
         return reverse("projects:project_detail", args=[str(self.id)])

    def save(self, *args, **kwargs):
        
        # Check if cretaor is  already a collaborator
        if self.created_by not in self.collaborators.all():
                self.collaborators.add(self.created_by)
        super().save(*args,**kwargs )

              
         
         
    




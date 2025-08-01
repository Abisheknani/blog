from typing import Any
from blog.models import Post,Category
from django.core.management.base import BaseCommand
import random



class Command(BaseCommand):
    help="This commands insert post data"

    def handle(self, *args: Any, **options: Any):
        #delete existing data
        Post.objects.all().delete()

        titles =[
            "Provides a comprehensive ",
            "Intriguing and  knowledge",
            "Action-time-sensitive",
            "Offers a structured approach",
            "Emphasizes current importance",
            "Offers a broad understanding",
            "Looks ahead at the evolution of a subject",
            "Focuses on proven methods",
            "Compares and contrasts",
            "Provides guidance for newcomers",
            "Offers in-depth knowledge",
            "Highlights a captivating aspect",
            "Beginner-friendly introduction",
            "Focuses on a positive result",
            "Addresses potential pitfalls",
            "Action-oriented and time-sensitive",
            "Emphasizes current importance",
            "Intriguing and reveals hidden knowledge",
            "Fouses on proven methods",
            "AI is tha powerfulll tool",

        ]

        contents =[
                "Health and lifestyle together is an issue that is always going to be in demand",
                "here are numerous articles, topics, data published on these topics regularly. The innumerable health",
                "Whether it is a script for a podcast, an explanation of a video, content writing is paramount to convey the information properly.",
                "This is why there is a huge demand for people wanting to know what would help them to improve ",
                "This type of content is always in demand since people are interested to know about whats happening in the relevant industries.",
                "Content writing topics on education can provide details on such courses and certificates. They should invoke the emotional as well as the practical aspects of a person.",
                "Select some of the topics that have a high search volume on this domain. Make sure you dedicate several ",
                "This is an extremely popular and always in-demand content writing topic. There are so many new job candidates every year.",
                "The prospect of appearing for an interview can be unnerving. These new professionals cover articles covering these topics",
                "This topic is a corollary of the above points. Nevertheless, problem-solving is one of the most widely read topics for any niche globally.",
                "The 5 Ws and 1H can be great topic titles for content topics that deal with problem-solving. The how, why, where, when, what questions can lay the premise for a great article.",
                "Every niche comes with its fair share of queries, and questions. If you provide satisfactory answers through your content,",
                "house content topics help to know about the characteristics of an organization and business. You learn how to co-ordinate",
                "give you a clear picture of how to develop and improve social skills and become an asset to your organization.",
                ". Also, several content topics in this niche help to imbibe the qualities of honesty and transparency.",
                "There are some pertinent best practices to create tutorials that would continue to reap the benefits in the long run. ",
                "topic is a corollary of the above points. Nevertheless, problem-solving is one of the most",
                "a clear picture of how to develop and improve social skills and become an asset ",
                "with its fair share of queries, and questions. If you provide satisfactory answers",
                "riting topics on education can provide details on such courses and certificates. ",
            ]                   

        img_urls =[
                "https://picsum.photos/id/1/800/400",
                "https://picsum.photos/id/2/800/400",
                "https://picsum.photos/id/3/800/400",
                "https://picsum.photos/id/4/800/400",
                "https://picsum.photos/id/5/800/400",
                "https://picsum.photos/id/6/800/400",
                "https://picsum.photos/id/7/800/400",
                "https://picsum.photos/id/8/800/400",
                "https://picsum.photos/id/9/800/400",
                "https://picsum.photos/id/10/800/400",
                "https://picsum.photos/id/11/800/400",
                "https://picsum.photos/id/12/800/400",
                "https://picsum.photos/id/13/800/400",
                "https://picsum.photos/id/14/800/400",
                "https://picsum.photos/id/15/800/400",
                "https://picsum.photos/id/16/800/400",
                "https://picsum.photos/id/17/800/400",
                "https://picsum.photos/id/18/800/400",
                "https://picsum.photos/id/19/800/400",
                "https://picsum.photos/id/20/800/400",
    
            ]


        categories = Category.objects.all()
        for title,content,img_url in zip(titles,contents,img_urls):
            category = random.choice(categories)
            Post.objects.create(title=title,content=content,img_url=img_url,category=category)

        self.stdout.write(self.style.SUCCESS("completed instert tha data."))

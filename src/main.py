import os
from input_parser import parse_input_text
from ppt_generator import generate_presentation
from template_manager import load_template, get_layout_mapping, print_layouts

def main():
    input_text = """
    # ChatPPT

    ## LGBTQIA+ Pride Month [Title ]

    ## Introduction [Right Pattern Content]
    - State the significance of LGBTQIA+ Pride Month
        - What is LGBTQIA+ Pride Month?
        - Why does the United States celebrate it?
        - How do other countries celebrate Pride?

    - Tell your story
        - What does LGBTQIA+ Pride Month mean to you?
        - Why is it important to you?
    
    ## Overview [Overview]
    
    - Give a brief overview of what you’ll cover in your presentation. 
    - 

    ## History [Chart Slide]
    - Make a timeline of the important historical events or list historical contributions made by the LGBTQIA+ Community.
    ![业绩图表](../images/performance_chart.png)

    ## Interesting facts [Left Pattern Content]
    - List some interesting facts about LGBTQIA+ Pride Month. Here are a few examples:
        The LGBT rights movement in the US was kickstarted in 1969 with the Stonewall riots.
        The rainbow flag was designed in 1978 by Gilbert Baker.
        President Obama announced the designation of the first national monument to LGBTQIA+ rights in 2016.


    ## Key People [Smart Art]
    - Choose three notable people of LGBTQIA+ Community using Bing.com and discuss their lives and accomplishments. Here are some examples: 

    ## Arts and literature [Two Photo Content]
    - Provide examples of art and literature that are significant to LGBTQIA+ Pride Month. Here are a few examples:
    - The writings of Patricia Highsmith
    - The music of Bessie Smith
    - The artwork of Keith Haring


    ## How to celebrate [Right Pattern Content Blue title]
    - List some ways you can celebrate LGBTQIA+ Pride Month. Here are a few examples:
    - Discover LGBTQIA+ artists
    - Read LGBTQIA+ authors
    - Listen to LGBTQIA+ musicians
    - Learn LGBTQIA+ history

    
    ## Conclusion [Questions]
    - Provide a brief summary of your presentation. Remind the audience what you covered in the previous slides.

    
    ## Questions & answers [Left Pattern Content Orange Title]
    - Invite questions from the audience.

    """

    template_file = '../templates/temp.pptx'
    prs = load_template(template_file)

    print("Available Slide Layouts:")
    print_layouts(prs)

    layout_mapping = get_layout_mapping(prs)

    powerpoint_data, presentation_title = parse_input_text(input_text, layout_mapping)

    output_pptx = f"../outputs/{presentation_title}.pptx"
    generate_presentation(powerpoint_data, template_file, output_pptx)

if __name__ == "__main__":
    main()

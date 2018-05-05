---
layout: page
permalink: /research/
title: Creative bioengineering
description: Innovation does not believe in academic borders. Neither do we! We use insights and methodologies from a variety of scientific and technological domains to meet our objectives.
---

<section id="why">
    <div class="container">
        <div class="row">
            <div class="col-lg-8 col-md-12 text-left">
                <h2 id = "main-space"><b>The BioFoundry</b></h2>
                <p>The BioFoundry at UBC utilizes metabolic &amp; enzyme engineering to investigate and customize novel biosynthetic enzymes that can convert biomass-derived feedstocks into better fuels, pharmaceuticals and value-added chemicals. We also extend these principles to the design and development of unique bioremediation strategies to rehabilitate the water quality in and around industrial zones and new mining technologies. In addition to green engineering, the BioFoundry also pursues medical biotechnology research, and we are working extensively on infectious disease drug discovery, drug delivery and tissue engineering.</p>
                <div id="responsive">
                    <img src="/img/research/research_overview.jpg" class="img-responsive">
                </div>
                <br>
                <p id="responsive-para"><b> Prof. Yadav </b> is an enthusiastic proponent of application-oriented science and knowledge translation for development of low-cost technologies, and the BioFoundry actively collaborates with local start-ups, industry, academic groups and medical research laboratories. Our work is fostering innovation in a strategic domain for Canada.</p>
                <p id="related_links"> </p>
            </div>
            <div class="col-lg-4 col-md-12 text-left research-large">
                <img class="img-responsive" src="/img/sustainable-ideas.jpg" >
                <h3 class="text-center"><a href="/research" class="button">About Us</a></h3>
                {% for project in site.projects %}
                {% if project.rel_link2 %}
                  <button type="button" class="list-group-item" onclick="loadData('{{project.long_desc}}','{{project.modal_image}}','{{project.rel_link}}','{{project.rel_linktxt}}','{{project.rel_link2}}','{{project.rel_linktxt2}}')" >{{project.title}}</button>
                {% elsif project.rel_link %}
                  <button type="button" class="list-group-item" onclick="loadData('{{project.long_desc}}','{{project.modal_image}}','{{project.rel_link}}','{{project.rel_linktxt}}')" >{{project.title}}</button>
                {% else%}
                <button type="button" class="list-group-item" onclick="loadData('{{project.long_desc}}','{{project.modal_image}}')" >{{project.title}}</button>

                {% endif %}  
                {% endfor %}                
            </div>           
        </div>
    </div>
    <div class="research-small">
        <div class="container">
            {% for project in site.projects %}
                <img src="{{project.front_image}}" class="img-responsive" alt="{{project.title}}" max-width="100%">
                <h1>{{project.title}}</h1>
                <p>{{project.long_desc}}</p>
                
            {% endfor %}
        </div>
    </div>
</section>

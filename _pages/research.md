---
layout: page
permalink: /research/
title: Research
description: Innovation does not believe in academic borders. Neither do we! We use insights and methodologies from a variety of scientific and technological domains to meet our objectives.
---

<section id="why">
    <div class="container">
        <div class="row">
            <div class="col-lg-8 col-md-12 text-left">
                <h2 id = "main-space"><b>The BioFoundry</b></h2>
                <p>We are a multidisciplinary research group that specializes in the design and development of next-generation, green chemical processes for the manufacture of cleaner fuels, superior medicines and novel materials.</p>
                <div id="responsive">
                    <img src="/img/research/research_overview.jpg" class="img-responsive">
                </div>
                <br>
                <p id="responsive-para"><b>The BioFoundry at the University of British Columbia</b> is a multidisciplinary research group that specialises in the development of green and sustainable chemical manufacturing processes and novel environmental remediation strategies. Our research group is at the forefront of innovation in a strategic domain for Canada and British Columbia. We utilise cutting-edge tools and technogloies to preicsely modulate and control the metabolic networks of microoganisms to produce cleaner fuels and more efficcacious drugs, as well as mop up pollution from the environment.</p>
            </div>
            <div class="col-lg-4 col-md-12 text-left research-large">
                <img class="img-responsive" src="/img/sustainable-ideas.jpg" >
                <h3 class="text-center"><a href="/research" class="button">About Us</a></h3>
                {% for project in site.projects %}
                  <button type="button" class="list-group-item" onclick="loadData('{{project.long_desc}}','{{project.modal_image}}')" >{{project.title}}</button>
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

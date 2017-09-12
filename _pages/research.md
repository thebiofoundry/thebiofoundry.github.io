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
                <p><b>The BioFoundry at the University of British Columbia</b> is a multidisciplinary research group that specialises in the development of green and sustainable chemical manufacturing processes and novel environmental remediation strategies. Our research group is at the forefront of innovation in a strategic domain for Canada and British Columbia. We utilise cutting-edge tools and technogloies to preicsely modulate and control the metabolic networks of microoganisms to produce cleaner fuels and more efficcacious drugs, as well as mop up pollution from the environment.</p>
                <br>
            </div>
            <div class="col-lg-4 col-md-12 text-left">
                <img class="img-responsive" src="/img/sustainable-ideas.jpg">
            </div>
            <div class="col-lg-8 col-md-8 text-left">
                <div id="responsive">
                    <h3>About the Group</h3>
                    <p>The oil industry has provided society with great wealth and power, fuel and energy, and materials and medicines for over 150 years. No force has shaped human society quite like oil has. But then again, neither has any other industry had as deleterious an impact on the environment.</p>
                    <p>Carbon dioxide released by the combustion of oil products has turned the planet into a sweltering greenhouse. Oceans are warming and glaciers are melting away, causing sea levels to rise, and if this trend persists, human settlements in low-lying coastal areas could soon be inundated with sea water.</p>
                    <p>A warming world, the threat of epidemics, our rapidly declining drug stocks, and the inefficiency of current manufacturing processes have forced the industry to reconfigure its operations along the principles of Green Chemistry & Engineering.</p>
                    <p>A warming world also threatens to unleash infectious diseases like never before. Unfortunately, though, antibiotic resistance is on the rise. Some microorganisms have already developed resistance to multiple drugs, and fewer antimicrobial drugs are being approved for use each year.</p>
                    <p>The new paradigm emphasizes improvements in the atom and energy efficiencies, and the environmental footprint of manufacturing processes by minimizing the generation of waste, eliminating the use of toxic reagents and solvents, utilizing renewable feedstocks, designing biodegradable products, and designing processes that minimize the likelihood of accidents. </p>
                    <p>To this end, biomass has emerged as a viable alternative to petroleum for the production of energy, chemicals and materials. Biomass is abundant, inexpensive and carbon neutral. Moreover, the immense ease and efficiency with which biological systems can convert biomass into fuels, chemicals and materials has generated renewed interest in biotechnology as a potential replacement for traditional chemical manufacturing processes. Nature’s powers of self-cleansing pollutants too remain unrivaled. </p>
                    <p>Aided by the ever-expanding repertoire of tools for studying microbial genetics and plant biotechnology, improved understanding of gene regulation and cellular metabolism, and incessantly accumulating gene and protein data, scientists & engineers such as us can now construct microbial cell factories to clean the environment, and produce fuels, chemicals, materials and pharmaceuticals in an economical and sustainable manner.  </p>
                </div>
            </div>
            <div class="col-lg-4 col-md-4 text-left">
                <br>
                <div class="list-group research-large">
                    <h3 ><b>Research Themes</b></h3>
                    <button  type="button" class="list-group-item" onclick="loadData('<h3>Research</h3>                    <p>The oil industry has provided society with great wealth and power, fuel and energy, and materials and medicines for over 150 years. No force has shaped human society quite like oil has. But then again, neither has any other industry had as deleterious an impact on the environment.</p>                    <p>Carbon dioxide released by the combustion of oil products has turned the planet into a sweltering greenhouse. Oceans are warming and glaciers are melting away, causing sea levels to rise, and if this trend persists, human settlements in low-lying coastal areas could soon be inundated with sea water.</p>                   <p>A warming world also threatens to unleash infectious diseases like never before. Unfortunately, though, antibiotic resistance is on the rise. Some microorganisms have already developed resistance to multiple drugs, and fewer antimicrobial drugs are being approved for use each year.</p>')" >Overview
                    </button>
                    <!-- <button type="button" class="list-group-item" onclick="loadData('{{site.projects[0].title}}')" >The Next Generation of Biofuels</button>
                    <button type="button" class="list-group-item">Better Chemistry for Synthesis of Better Drugs</button>
                    <button type="button" class="list-group-item">Biocatalysis for the Biorefinery</button>
                    <button type="button" class="list-group-item">Drug Delivery &amp; Formulations</button>
                    <button type="button" class="list-group-item">Fighting Malaria with Synthetic Biology</button>
                    <button type="button"  class="list-group-item" id= "Neuroengineering"> Neuroengineering </button>
                    <button type="button" id="Biomanufacturing" class="list-group-item">Advanced Biomanufacturing</button>
                    <button type="button" class="list-group-item">Environmental Stewardship &amp; Bioremediation</button>    -->
                    {% for project in site.projects %}
                      <button type="button" class="list-group-item" onclick="loadData('{{project.long_desc}}','{{project.modal_image}}')" >{{project.title}}</button>
                    {% endfor %}
                </div>
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

<section id="why">
<div class="container">
    <div class="row">
        <div class="col-lg-12 text-center">
            <h1><b>Issues</b></h1>
            <hr />
            <br>
        </div>
    </div>
</div>

<div class="container">
    <div class="row">
        <div class="col-lg-3 col-md-6 text-center">
            <div class="service-box" id= "bioFuels">
                <i class="fa fa-4x fa-bolt wow bounceIn text-primary"></i>
                <h3>Global Warming</h3>
                <p class="text-muted">Our templates are updated regularly so they don't break.</p>
            </div>
        </div>
        <div class="col-lg-3 col-md-6 text-center">
            <div class="service-box" >
                <i class="fa fa-4x fa-life-ring wow bounceIn text-primary" data-wow-delay=".1s"></i>
                <h3>Rising Seas</h3>
                <p class="text-muted">You can use this theme as is, or you can make changes!</p>
            </div>
        </div>
        <div class="col-lg-3 col-md-6 text-center">
            <div class="service-box">
                <i class="fa fa-4x fa-medkit wow bounceIn text-primary" data-wow-delay=".2s"></i>
                <h3>Epidemics</h3>
                <p class="text-muted">We update dependencies to keep things fresh.</p>
            </div>
        </div>
        <div class="col-lg-3 col-md-6 text-center">
            <div class="service-box">
                <i class="fa fa-4x fa-cutlery wow bounceIn text-primary" data-wow-delay=".3s"></i>
                <h3>Famine</h3>
                <p class="text-muted">You have to make your websites with love these days!</p>
            </div>
        </div>
        <hr />
    </div>
</div>
</section>

<section class="cta">
    <div class="cta-content">
        <div class="container">
            <h2>Join us. Get<br>in touch.</h2>
            <a href="/contact" class="btn btn-outline btn-xl page-scroll">Contact</a>
        </div>
    </div>
    <div class="overlay"></div>
</section>




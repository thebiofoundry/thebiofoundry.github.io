---
layout: page
permalink: /members/
title: BioFoundry Members
description: Current members and alumni
---
<!-- <link rel="stylesheet" href="{{ '/assets/css/members.css' | prepend: site.baseurl | prepend: site.url }}"> -->
<br>

<div class="container">
	
	<!-- Beginning of PI -->
	<h3>Principal Investigator</h3>
	<hr style="border-top: 1px solid #8c8b8b; max-width: 100%!important;"><br>
	<div class="row">
	{% for member in site.members %}
	{% if member.status == 'pi' %}
	<div class="col-md-3 col-sm-6 member-block">
		<div class= "pop-block" title="<h2>{{ member.title }} </h2> <br> {{member.degrees}}" data-toggle="popover" data-container="body" tabindex="0" data-placement = "bottom"  data-content="<b>Research Focus:</b><br> {{member.description}} <br><br> <b>Something About Me:</b> <br> {{member.about_me}}">
		            <center>
		            	{% if member.img  %}
						<img src="{{ member.img | prepend: site.baseurl | prepend: site.url }}" class = "member-img">
						{% else %}
						<img src="{{ site.generic_image | prepend: site.baseurl | prepend: site.url }}" class = "member-img">
						{% endif %}
		            </center>
		</div>
<br>
	<div class= "member-spacer">
	    <b> {{ member.title }} </b> 
	    <small>{{ member.program }} | since {{ member.year_start }} </small>
	</div>
	</div>
	{% endif %}
	{% endfor %}
	</div>
	<!-- End of PI -->
	
	
	<!-- Beginning of Post-doc -->
	<h3>Postdoctoral Researchers</h3>
	<hr style="border-top: 1px solid #8c8b8b; max-width: 100%!important;"><br>
	<div class="row">
	{% for member in site.members %}
	{% if member.status == 'postdoc' %}
	<div class="col-md-3 col-sm-6 member-block">
		<div class= "pop-block" title="<h2>{{ member.title }} </h2> <br> {{member.degrees}}" data-toggle="popover" data-container="body" tabindex="0" data-placement = "bottom"  data-content="<b>Research Focus:</b><br> {{member.description}} <br><br> <b>Something About Me:</b> <br> {{member.about_me}}">
		            <center>
		            	{% if member.img  %}
						<img src="{{ member.img | prepend: site.baseurl | prepend: site.url }}" class = "member-img">
						{% else %}
						<img src="{{ site.generic_image | prepend: site.baseurl | prepend: site.url }}" class = "member-img">
						{% endif %}
		            </center>
		</div>
<br>
	<div class= "member-spacer">
	    <b> {{ member.title }} </b> 
	    <small>{{ member.program }} | since {{ member.year_start }} </small>
	</div>
	</div>
	{% endif %}
	{% endfor %}
	</div>
	<!-- End of Post-doc -->
	<!-- Beginning of Grad -->
	<h3>Graduate Students</h3>
	<hr style="border-top: 1px solid #8c8b8b; max-width: 100%!important;"><br>
	<div class="row">
	{% for member in site.members %}
	{% if member.status == 'grad' %}
	<div class="col-md-3 col-sm-6 member-block">
		<div class= "pop-block" title="<h2>{{ member.title }} </h2> <br> {{member.degrees}}" data-toggle="popover" data-container="body" tabindex="0" data-placement = "bottom"  data-content="<b>Research Focus:</b><br> {{member.description}} <br><br> <b>Something About Me:</b> <br> {{member.about_me}}">
		            <center>
		            	{% if member.img  %}
						<img src="{{ member.img | prepend: site.baseurl | prepend: site.url }}" class = "member-img">
						{% else %}
						<img src="{{ site.generic_image | prepend: site.baseurl | prepend: site.url }}" class = "member-img">
						{% endif %}
		            </center>
		</div>
<br>
	<div class= "member-spacer">
	    <b> {{ member.title }} </b> 
	    <small>{{ member.program }} | since {{ member.year_start }} </small>
	</div>
	</div>
	{% endif %}
	{% endfor %}
	</div>
<!-- End of Grad  -->
<!-- Undergraduate line -->

<h3>Undergraduate Students</h3>
<hr style="border-top: 1px solid #8c8b8b; max-width: 100%!important;"><br>
<div class="row">
	{% for member in site.members %}
	{% if member.status == 'undergrad' %}
	<div class="col-md-3 col-sm-6 member-block">
		<div class= "pop-block" title="<h2>{{ member.title }} </h2> <br> {{member.degrees}}" data-toggle="popover" data-container="body" tabindex="0" data-placement = "bottom"  data-content="<b>Research Focus:</b><br> {{member.description}} <br><br> <b>Something About Me:</b> <br> {{member.about_me}}">
		            <center>
		            	{% if member.img %}
						<img src="{{ member.img | prepend: site.baseurl | prepend: site.url }}" class = "member-img">
						{% else %}
						<img src="{{ site.generic_image | prepend: site.baseurl | prepend: site.url }}" class = "member-img">
						{% endif %}
		            </center>
		</div>
		            <br>
		            <div class= "member-spacer">
			            <b> {{ member.title }} </b> 
			            <small>{{ member.program }} | since {{ member.year_start }} </small>
		            </div>
	</div>
	{% endif %}
	{% endfor %}
	</div>
	<!-- End of Undergrad -->
</div>



<br>

 <script src="https://code.jquery.com/jquery-1.9.1.js"></script>
 <script src="https://code.jquery.com/jquery-migrate-1.1.0.js"></script>

<script>
	$(document).ready(function(){
    $('[data-toggle="popover"]').popover({html: true}); });
	

	$('body').on('click', function (e) {
	    $('[data-toggle="popover"]').each(function () {
	        //the 'is' for buttons that trigger popups
	        //the 'has' for icons within a button that triggers a popup
	        if (!$(this).is(e.target) && $(this).has(e.target).length === 0 && $('.popover').has(e.target).length === 0) {
	            $(this).popover('hide');
	        }
	    });
	});
</script>



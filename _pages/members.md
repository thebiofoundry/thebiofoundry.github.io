---
layout: page
permalink: /members/
title: BioFoundry Members
description: Current members and alumni
---

<!-- <link rel="stylesheet" href="{{ '/assets/css/members.css' | prepend: site.baseurl | prepend: site.url }}"> -->

<br>
<div class="container">
	<h3>Graduate students</h3>
	<hr style="border-top: 1px solid #8c8b8b; max-width: 100%!important;"><br>
	<div class="row">
	{% for member in site.members %}
	{% if member.status == 'grad' %}
	<div class="col-md-3 col-sm-6 member-block">
		<div class= "pop-block" title="<h2>{{ member.title }} </h2> <br> {{member.degrees}}" data-toggle="popover" data-trigger="focus" tabindex="0" data-placement = "bottom"  data-content="<b>Research Focus:</b><br> {{member.description}} <br><br> <b>Something About Me:</b> <br> {{member.about_me}}">
		            <center>
		            	<img src="{{ member.img | prepend: site.baseurl | prepend: site.url }}" class = "member-img">
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
	<!-- Undergraduate line -->
	<h3>Undergraduate students</h3>
	<hr style="border-top: 1px solid #8c8b8b; max-width: 100%!important;"><br>
	<div class="row">
	{% for member in site.members %}
	{% if member.status == 'undergrad' %}
	<div class="col-md-3 col-sm-6 member-block">
		<div class= "pop-block" title="<h2>{{ member.title }} </h2> <br> {{member.degrees}}" data-toggle="popover" data-trigger="focus" tabindex="0" data-placement = "bottom"  data-content="<b>Research Focus:</b><br> {{member.description}} <br><br> <b>Something About Me:</b> <br> {{member.about_me}}">
		            <center>
		            	<img src="{{ member.img | prepend: site.baseurl | prepend: site.url }}" class = "member-img">
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
</div>


<br>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
<script>
$(document).ready(function(){
    $('[data-toggle="popover"]').popover({html: true});   
});
</script>
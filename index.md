![banner]({{site.url}}/content/shared/img/banner.svg)

This is the website for the course PSYCH101-D,
**Data Science for Research Psychology**,
taught at UC Berkeley in Fall 2019.

## Course Description

Experimental and data science abound with models.
Models of data can be used
to _simulate_, as in models of the climate,
to _explain simply_, as in paper airplanes,
and to _predict_, as in prototype models;
all of these are forms of inferential thinking.
In this course, we will learn to use Python
to describe, create, manipulate, and interrogate models of data.
With these new skills,
we will simulate, explain, and predict phenomena and data,
drawing examples from research psychology.
As one application of these tools,
we will develop classical statistical approaches,
like null hypothesis significance testing and linear regression.

## Course Materials

{% capture materialtable  %}{% include materialtable.md %}{% endcapture %}
{{ materialtable | markdownify }}

## How to Use the Materials

The table above has links to all of the materials for the course.
Either one will drop you into a cloud-computing environment in your browser,
where you can review lectures, complete homeworks and labs, and get scores on autograded sections.

### Berkeley Users

The links which look like
![interact]({{site.url}}/content/shared/img/interact_badge.svg),
are for use by **Berkeley-affiliated folks**.
After logging in with your CalNet ID,
you'll be dropped into `datahub.berkeley.edu`,
where a copy of the course materials, plus any file you add,
will be maintained for your own use.
_If you've never used this service_, check out [this video](https://data.berkeley.edu/file/327).

### Non-Berkeley Users

The links which look like
![Binder](https://mybinder.org/badge_logo.svg),
are for use by **non-Berkeley-affiliated folks**,
i.e. anyone without a CalNet ID.
After clicking on these, you'll need to wait through a short (<2 min) build period.
If you encounter an error during this build, click the link a second time.
If the build still fails, contact the course staff.

Once the build succeeds,
you'll be dropped into a temporary cloud environment,
where you can look through and edit the materials,
but any changes you make will not be saved.
You can still complete homeworks and labs and get scores on autograded sections.
If you stop interacting with the material (viewing pages, clicking, typing)
for an extended period (~20 minutes), your environment will be deleted.
If you need to step away while working, you can download assignments to your local machine,
using the file menu in the Jupyter notebok,
and then reupload them using the Upload button in the Jupyter file browser.

If you're not Berkeley-affiliated and would like a persistent copy of the course materials,
you'll need to perform a local installation of the environment
using `git`, GitHub, and `pip`.
See instructions below.


### Local Installation

For instructions on local installation, see
[the GitHub repository](https://github.com/charlesfrye/psych101d)
where the materials are stored.

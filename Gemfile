source 'https://rubygems.org'

gem 'asciidoctor'
gem 'asciidoctor-pdf'
gem 'asciidoctor-bibtex'
gem "jekyll", "~> 3.8.1"
gem 'coderay'
gem 'rake-jekyll', '~> 1.1.0'

# Added at 2018-05-03 20:56:04 -0500 by chief\ryan:
gem "unicode_utils", "~> 1.4"

gem "minima", "~> 2.0"

group :jekyll_plugins do
  gem 'jekyll-asciidoc'
  gem "jekyll-feed", "~> 0.10"
  gem 'asciidoctor-bibtex' #Needs to be here to automatically run on jekyll adoc files
end

# Windows does not include zoneinfo files, so bundle the tzinfo-data gem
gem "tzinfo-data", platforms: [:mingw, :mswin, :x64_mingw, :jruby]

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.0" if Gem.win_platform?

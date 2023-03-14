# config.ru

dev = ENV['RACK_ENV'] == 'development'

require 'rack/unreloader'

Unreloader = Rack::Unreloader.new(:subclasses=>%w'Sinatra::Base', :reload=>dev){Tarot_App}
Unreloader.require './tarot_app.rb'

run(dev ? Unreloader : Tarot_App)
# config.ru

dev = ENV['RACK_ENV'] == 'development'

require 'rack/unreloader'

Unreloader = Rack::Unreloader.new(:subclasses=>%w'Sinatra::Base', :reload=>dev){Ruby_Tarot}
Unreloader.require './ruby_tarot.rb'

run(dev ? Unreloader : Ruby_Tarot)